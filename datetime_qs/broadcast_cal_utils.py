"""util functions for broadcast calendar

   https://en.wikipedia.org/wiki/Broadcast_calendar
"""

import datetime


def broadcast_month_start(year, month):
    """return start of broadcast month. always on monday"""
    start_date = datetime.datetime(year, month, 1)
    while start_date.weekday() != 0:
        start_date -= datetime.timedelta(days=1)
    return start_date

def quarter_start_month(quarter):
    """month that starts quarter for Gregorian calendar: Jan, Apr, Jul, Oct"""
    if quarter not in range(1, 5):
        raise ValueError("invalid quarter")
    return 3 * (quarter - 1) + 1

def next_quarter(year, quarter):
    """return next quarter for Gregorian calendar"""
    if quarter not in range(1, 5):
        raise ValueError("invalid quarter")
    if quarter == 4:
        return year+1, 1
    else:
        return year, quarter+1

def broadcast_quarter_dates(year, quarter):
    """start and end dates for broadcast quarter"""
    month = quarter_start_month(quarter)
    start = broadcast_month_start(year, month)

    # calculate end of quarter based on start of next quarter
    year, quarter = next_quarter(year, quarter)
    month = quarter_start_month(quarter) #maybe have next_quarter return month too?
    end = broadcast_month_start(year, month) - datetime.timedelta(days=1)

    return start, end

def get_quarter(month):
    """return quarter for month"""
    if month not in range(1, 13):
        raise ValueError("invalid month")
    # https://stackoverflow.com/a/1406182
    # User: Alex Martelli
    # https://stackoverflow.com/users/95810/alex-martelli
    return (month - 1) // 3 + 1

def next_quarter_broadcast_dates():
    """return dates for next broadcast quarter (from now)"""
    now = datetime.datetime.today()
    year = now.year
    quarter = get_quarter(now.month)
    while True:
        start, end = broadcast_quarter_dates(year, quarter)
        if now < start:
            return start, end
        year, quarter = next_quarter(year, quarter)

def next_monday():
    """return datetime for next monday"""
    temp = datetime.datetime.today()
    # *next* monday, don't return today if it's monday
    while True:
        temp += datetime.timedelta(days=1)
        if temp.weekday() == 0:
            return temp
