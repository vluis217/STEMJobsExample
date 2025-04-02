#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

headers = {
    "User-Agent": userAgent
}

url = "https://www.google.com/about/careers/applications/jobs/results/?location=Colombia"

session = requests.Session()

response = session.get(url=url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

jobs = soup.find_all(class_ = "sMn82b")

for job in jobs:
    print(f"ID: {job.a["href"].split("/")[2].split("-")[0]}")
    print(f"Título: {job.h3.text}")
    print(f"Empresa: {job.find(class_ = "RP7SMd").span.text}")
    print(f"Nivel de experiencia: {job.find(class_ = "wVSTAb").text}")
    print(f"Ubicación: {job.find(class_ = "r0wTof").text}")
    print(f"Link: https://www.google.com/about/careers/applications/{job.a["href"]}")
    print()
