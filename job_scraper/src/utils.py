import csv
import json


def save_data(file_path, method="w", jobs_info=None, work_title=None,
              company_name=None, city=None, min_salary=None,
              max_salary=None, url=None):
    if method == "w" and jobs_info == None:
        with open(file_path, method) as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    "work_title",
                    "company_name",
                    "city",
                    "min_salary",
                    "max_salary",
                    "url"
                )
            )
    elif method == "a" and jobs_info == None:
        with open(file_path, method) as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    work_title,
                    company_name,
                    city,
                    min_salary,
                    max_salary,
                    url
                )
           )
    if jobs_info != None:
        with open(file_path, method) as file:
            json.dump(jobs_info, file, indent=4, ensure_ascii=False)   

