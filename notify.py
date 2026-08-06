import requests
import json
from datetime import datetime

TOPIC = "whsCalendarSchedule"

# Load JSON file
with open("schooldays.json", "r") as file:
    school_days = json.load(file)


def get_day_type(date):
    for day_type, dates in school_days.items():
        if date in dates:
            return day_type
    
    return "Unknown"


def send_notification(today, y, m, d):
    monthDictionary = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
    }
    dayDictionary = {
        "01": "1st",
        "02": "2nd",
        "03": "3rd",
        "04": "4th",
        "05": "5th",
        "06": "6th",
        "07": "7th",
        "08": "8th",
        "09": "9th",
        "10": "10th",
        "11": "11th",
        "12": "12th",
        "13": "13th",
        "14": "14th",
        "15": "15th",
        "16": "16th",
        "17": "17th",
        "18": "18th",
        "19": "19th",
        "20": "20th",
        "21": "21st",
        "22": "22nd",
        "23": "23rd",
        "24": "24th",
        "25": "25th",
        "26": "26th",
        "27": "27th",
        "28": "28th",
        "29": "29th",
        "30": "30th",
        "31": "31st"
    }

    

    day_type = get_day_type(today)

    if day_type == "A" or day_type == "B":
        message = f"Today is a {day_type} day"
    elif day_type == "FINALS":
        message = f"There are {day_type} today, Good Luck!"
    else:
        message = "There is no school today"

    requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message,
        headers={
            "Title": f"{monthDictionary[month]} {dayDictionary[day]}, {year}",
            "Priority": "urgent"
        }
    )

    return message

def main():

    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")
    
    # Testing
    year = "2026"
    month = "09"
    day = "09"
    
    # today = datetime.now().strftime("%Y-%m-%d")
    today = "2026-09-09"

    send_notification(today, year, month, day)
    print(f"Today's Date: {today}")
    print(f"Notification Sent: {send_notification(today)}")
    

if __name__ == "__main__":
    main()