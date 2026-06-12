import requests

url = "https://www.jpsc.gov.in/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers,
    timeout=60
)

print(response.status_code)
print("Downloaded", len(response.text), "characters")
