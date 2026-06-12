import os
import requests

url = "https://www.jpsc.gov.in/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=60)

current_length = len(response.text)

try:
    with open("last_length.txt", "r") as f:
        old_length = int(f.read().strip())
except:
    old_length = 0

if current_length != old_length:

    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    message = (
        "🚨 JPSC website updated!\n\n"
        "https://www.jpsc.gov.in/"
    )

    requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data={
            "chat_id": chat_id,
            "text": message
        }
    )

    with open("last_length.txt", "w") as f:
        f.write(str(current_length))

    print("Change detected. Telegram sent.")

else:
    print("No change detected.")
