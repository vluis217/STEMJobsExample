#!/usr/bin/python3

import requests

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

headers = {
    "User-Agent": userAgent
}

url = "https://careers.google.com/api/v3/search/?location=Colombia&sort_by=date"

session = requests.Session()

response = session.get(url=url, headers=headers)

jobs = response.json()["jobs"]

for job in jobs:
    print(f"ID: {job["id"].split("/")[1]}")
    print(f"Título: {job["title"]}")
    print(f"Empresa: {job["company_name"]}")
    print(f"Categoría: {job["categories"][0]}")
    print(f"Nivel de experiencia: {job["target_level"]}")
    print(f"Ubicación: {job["locations"][0]["display"]}")
    print(f"Link: https://www.google.com/about/careers/applications/jobs/results/{job["id"].split("/")[1]}")
    print()
