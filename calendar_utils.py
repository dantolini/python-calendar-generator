
from datetime import date, timedelta

events = {
    '01-01': "New Years Day",
    '01-26': "Australia Day",
    '03-08': "Labour Day",
    '03-26': "Good Friday",
    '03-28': "Easter Sunday",
    '03-29': "Easter Monday",
    '04-25': "ANZAC Day",
    '06-14': "King's Birthday",
    '09-24': "Grand Final Parade (proj.)",
    '11-02': 'Melbourne Cup Day',
    '12-25': 'Christmas Day',
    '12-27': 'Christmas Day Holiday',
    '12-26': 'Boxing Day',
    '12-28': 'Boxing Day Holiday'
}

def get_event(date):
    key = date.strftime("%m-%d")
    return events.get(key)

def get_monday(date):
    return date - timedelta(date.weekday())
