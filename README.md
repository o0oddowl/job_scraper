# Job Scraper: Work.ua & Robota.ua
This project is a web scraper that collects job vacancies from [Work.ua](https://www.work.ua/) and [Robota.ua](https://robota.ua/).  
It enables the collection, storage, and analysis of up-to-date job listings in Ukraine.

---

## 📄 Data Fields Collected(JSON, CSV):
- **work_title** – job title
- **company** – company name
- **city** – city
- **min_salary** – minimum salary in UAH
- **max_salary** – maximum salary in UAH
- **url** – link to the job vacancy

---

## Output Data (JSON):
```bash
 {
    "work_title": "Адміністратор офісу, офіс-менеджер",
    "company": "Красюк О.В., ФОП",
    "city": "Харків",
    "min_salary": 25000,
    "max_salary": 40000,
    "url": "https://www.work.ua/jobs/6955552/"
}
```

## Output Data (CSV):
```bash
work_title,company_name,city,min_salary,max_salary,url                                                                                                                                                                                 
"Адміністратор офісу, офіс-менеджер","Красюк О.В., ФОП","Харків, ",25000,40000,https://www.work.ua/jobs/6955552/
"Менеджер з продажу, оренди нерухомості (з навчанням, ст. м. Золоті Ворота)","Flatprime, АН","Київ, ",60000,120000,https://www.work.ua/jobs/5976294/
 Касир в магазин Nike,Делта Спорт,"Київ, ",28000,30000,https://www.work.ua/jobs/6910303/
 Садівник,TOPIAR,"Київ, ",30000,45000,https://www.work.ua/jobs/6572533/
```

---

## 📁 Project Structure:
```text
job_scraper/
├── src/
│ ├── scraper/
│ │ ├── robotaua_scraper.py
│ │ └── workua_scraper.py
│ └── utils.py
│
├── data/
│ ├── robotaua_data.json # Created when script is run
│ ├── robotaua_raw_data.csv # Created when script is run
│ ├── workua_data.json # Created when script is run
│ └── workua_raw_data.csv # Created when script is run
│
├── html_file/
│ └── robotauapage1.html, robotauapage2.html, ..., ~robotauapage5000.html # HTML pages saved by the script
│
└── requirements.txt
```
---

## ⚙️ Requirements:
- Python 3.11
- Firefox (used with Selenium — can be replaced with another browser in the code)

### Python Libraries:
Install dependencies using:
```bash
pip install -r requirements.txt
```
---

## 🚀 Running the Scrapers:
To run the Work.ua scraper:
```bash
python3.11 -m src.scraper.workua_scraper
```
To run the Robota.ua scraper:
```bash
python3.11 -m src.scraper.robotaua_scraper
```
---
Note: A `main.py` file was considered for simplified execution, but the decision was made to run scrapers individually.

