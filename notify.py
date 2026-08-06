import requests
import json
import os
from datetime import datetime

TOPIC = os.environ["NTFY_TOPIC"]

# Load JSON file
with open("schooldays.json", "r") as file:
    school_days = json.load(file)


def get_day_type(date):
    for day_type, dates in school_days.items():
        if date in dates:
            return day_type
    
    return "Unknown"


def send_notification(today):

    day_type = get_day_type(today)

    if day_type == "A" or day_type == "B":
        message = f"Today is a {day_type} day"
    elif day_type == "FINALS":
        message = f"There are {day_type} today, Good Luck!"
    else:
        message = "There is no school today"

    
    title = datetime.now().strftime("%B %-d, %Y")

    response = requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message,
        headers={
            "Title": title,
            "Priority": "urgent"
        }
    )

    if response.status_code == 200:
        print("Notification sent!")
    else:
        print("Failed:", response.status_code)

    return message

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    # today = "2026-09-09"

    print(send_notification(today))
    send_notification(today)
    

if __name__ == "__main__":
    main()
