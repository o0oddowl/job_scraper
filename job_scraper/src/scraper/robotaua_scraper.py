import json
import csv
import random
import time
import re

from bs4 import BeautifulSoup
from selenium import webdriver

from utils import save_data


def selenium(page=""):
    driver = webdriver.Firefox()
    try:
        driver.get(f"https://robota.ua/zapros/ukraine/params;{page}")
        time.sleep(1)
        
        height = 100 + driver.execute_script("return document.body.scrollHeight")
        for i in range(0, height, 900):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.1)

        with open(f"../html_file/robotaua{page}.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
    except Exception as e:
        print(e)
    finally:
        driver.quit()


def get_page():
    selenium("page=1")
    with open("../html_file/robotauapage=1.html") as file:
        scr = file.read()
    soup = BeautifulSoup(scr, "lxml")
    page = soup.find("div", class_="paginator").find_all("a")[-2].text
    return int(page)


def scraper():
    page = get_page()
    save_data("../data/robotaua_raw_data.csv")    
    
    jobs_info = []
    for page_num in range(page, 0, -1):
        selenium(f"page={page_num}")
        with open(f"../html_file/robotauapage={page_num}.html") as file:
            scr = file.read()
        soup = BeautifulSoup(scr, "lxml")

        job_list = soup.find_all("div", class_="santa--mb-20")
        for jobs in job_list:
            try:
                work_title = jobs.find("h2").text
                company = jobs.find("div", class_="santa-flex").find("span", class_="santa-mr-20").text.strip()
                
                city_list = jobs.find("div", class_="santa-flex").find("span", class_="santa-mr-20").find_next("span").text.strip().split(" ")
                city_list = list(filter(None, city_list))
                if len(city_list) < 3:
                    city = city_list[0]
                else:
                    city = jobs.find("div", class_="santa-flex").find("span", class_="santa-mr-20").find_next("span").find_next("span").text.strip().split(" ")[0]

                salary = jobs.find("div", class_="santa-flex").find("span").text[:-5].replace(" ","").split("—")
                try:
                    if len(salary) > 1:
                        min_salary, max_salary = int(salary[0]), int(salary[1])
                    else:
                        min_salary, max_salary = 0, int(salary[0])
                except:
                    min_salary, max_salary = 0, 0
                url = "https://robota.ua" + jobs.find("a", class_="card", href=True)["href"]
                jobs_info.append({
                    "work_title":work_title,
                    "company":company,
                    "city":city,
                    "min_salary":min_salary,
                    "max_salary":max_salary,
                    "url":url
                })
                save_data("../data/robotaua_raw_data.csv", "a", None, work_title, company, city, min_salary, max_salary, url)
            except Exception as e:
                print("ERROR:", e)
    save_data("../data/robotaua_data.json","w", jobs_info)

def main():
    scraper()

if __name__ == "__main__":
    main()
