import datetime as dt

def newYear():
    current_date = dt.datetime.now()
    new_year = dt.datetime(current_date.year + 1, 1, 1)
    return (new_year - current_date).days