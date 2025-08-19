import json
import csv
import random
import time

import requests
import fake_useragent
from bs4 import BeautifulSoup

from utils import save_data


def param(link):
    ua = fake_useragent.UserAgent().random
    headers={
        "user-agent":ua
    }
    r = requests.get(link, headers=headers).text
    soup = BeautifulSoup(r, "lxml")
    return soup


def get_page():
    soup = param("https://www.work.ua/jobs/?page=1")
    page = soup.find("ul", class_=["pagination", "hidden-xs"]).find_all("a")[-2].text
    return int(page)


def scraper():
    page = get_page()
    seen_urls = set()
    jobs_info = []
    save_data("../data/workua_raw_data.csv")
     
    for page_num in range(1,page+1):
        print(f"Process:{page_num}/{page}", end="\r", flush=True)
        if page_num > 0 and page_num % 1000 == 0:
            time.sleep(30)
        soup = param(f"https://www.work.ua/jobs/?page={page_num}")
        job_list = soup.find_all("div", class_=["card card-hover", "card-visited", "wordwrap", "job-link", "js-hot-block"]) 
        for jobs in job_list:
            try:
                work_title = jobs.find("div", class_="mb-lg").find("h2", class_="my-0").text.strip()
                company = jobs.find("div", class_="mt-xs").find("span", class_="mr-xs").find("span", class_="strong-600").text
            except:
                continue
            try:
                city = (jobs.find("div", class_="mt-xs").find("ul", class_=["list-unstyled", "my-0", "sm:mr-xs", "inline-block"])
                        .find_all("li")[-1].find_next("span").find_next("span").find_next("span")).text
            except:
                city = jobs.find("div", class_="mt-xs").find_all("span")[-1].text
            try:
                salary = jobs.find("span", class_="strong-600").text[0:-4].replace("\u202F", "").split("–")
                if len(salary) > 1:
                    min_salary, max_salary = int(salary[0]), int(salary[1])
                else:
                    min_salary, max_salary = 0, int(salary[0])
            except:
                min_salary = max_salary = 0
            url = "https://www.work.ua" + jobs.find("div", class_="mb-lg").find("h2", class_="my-0").find("a", href=True)["href"]
            if not url in seen_urls:
                seen_urls.add(url)
                save_data("../data/workua_raw_data.csv" ,"a", None, work_title, company, city, min_salary, max_salary, url)
                jobs_info.append({
                    "work_title":work_title,
                    "company":company,
                    "city":city,
                    "min_salary":min_salary,
                    "max_salary":max_salary,
                    "url":url
                })
        save_data("../data/workua_data.json","w", jobs_info)


def main():
    scraper()

if __name__ == "__main__":
    main()
