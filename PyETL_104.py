
import requests
from bs4 import BeautifulSoup
import os
import csv

url = "https://www.104.com.tw/jobs/search/?ro=0&keyword=%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=1&asc=0&page={}&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

file = open("TGI102_15_AliceChiu.csv", "a", newline="", encoding='utf8')
csv_writer = csv.writer(file)
csv_writer.writerow(["職稱", "公司名稱", "產業類別"])

page = 1
for c in range(0, 5):
    res = requests.get(url.format(page), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    article_tags = soup.select('article[class="b-block--top-bord job-list-item b-clearfix js-job-item"]')  # 取得article標籤
    for i in article_tags:
        Job = i.get('data-job-name')
        Company = i.get('data-cust-name')
        Industry = i.get('data-indcat-desc')
        csv_writer.writerow([Job, Company, Industry])
    page += 1
file.close()