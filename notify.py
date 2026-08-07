import requests
import json
from datetime import datetime
from zoneinfo import ZoneInfo

TOPIC = "whsCalendarSchedule"
TIMEZONE = "America/Los_Angeles"  # change to your timezone if different

# Load JSON file
with open("schooldays.json", "r") as file:
    school_days = json.load(file)

def getDayType(date):
    matches = [] # empty array
    for day_type, dates in school_days.items():
        if date in dates:
            matches.append(day_type)  # find matches in JSON file for the date parameter
    return matches # return array

def getMessage(today):
    day_types = getDayType(today) # get day types of today's day
    if not day_types or "no school" in day_types: # if no types or no school then the output is no school
        message = "There is no school today"
    elif "FINALS" in day_types: # if there are finals
        message = "There are FINALS today, Good Luck!"
    else:
        ordered_types = [] # empty array
        for i in ["Collab", "Min", "A", "B"]: # repeat for collab, min, a, and b
            if i in day_types: # if collab, min, a, or b are in day_types
                ordered_types.append(i) # add to types array
        message = f"Today is a {' '.join(ordered_types)} day" # combined message
    return message

def sendNotification(msg):
    now_local = datetime.now(ZoneInfo(TIMEZONE)) # current time in your local timezone
    title = now_local.strftime("%B %-d, %Y") # today's date, localized
    # send notification
    response = requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=msg,
        headers={
            "Title": title,
            "Priority": "urgent"
        }
    )
    # console message
    if response.status_code == 200:
        print("Notification sent!")
    else:
        print("Failed:", response.status_code)
    #return message

def main():
    today = datetime.now(ZoneInfo(TIMEZONE)).strftime("%Y-%m-%d") # today's date in your local timezone
    message = getMessage(today)
    sendNotification(message)

# if __name__ == "__main__":
#     main()
