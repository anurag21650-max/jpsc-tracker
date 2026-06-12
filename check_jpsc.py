import requests
from bs4 import BeautifulSoup

url = "https://www.jpsc.gov.in/"
html = requests.get(url, timeout=30).text

with open("latest_jpsc_page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("JPSC page downloaded successfully")
