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

## 📁 Project Structure
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
├── README.md
└── requirements.txt

---

## ⚙️ Requirements
- Python 3.11
- Firefox (used with Selenium — can be replaced with another browser in the code)

### Python Libraries
Install dependencies using:
```bash
pip install -r requirements.txt
```
---

## 🚀 Running the Scrapers
To run the Work.ua scraper:
    python3.11 -m src.scraper.workua_scraper
To run the Robota.ua scraper:
    python3.11 -m src.scraper.robotaua_scraper

Note: A `main.py` file was considered for simplified execution, but the decision was made to run scrapers individually.

