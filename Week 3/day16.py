# Day 16 - Python Date time

from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

# Formatting
# German Timestamp:
timestamp = now.strftime('%d.%m.%Y %H:%M:%S')
print(timestamp)
new_year = datetime(2025, 1, 1)
print(new_year)
print(f"{new_year.day}.{new_year.month}.{new_year.year}")
print(new_year.strftime("%d.%m.%Y - %A/%a - %B/%b - %Y/%y - DayNumber of Year = %j - %c - %x - %X"))

# String to Time
date_string = "13 June, 2006"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

########################################################################
print("########################################################################")
########################################################################

#1
current = datetime.now()
print(current)
print(current.year)
print(current.month)
print(current.day)

#2
formatted_date = datetime.strftime(current, "%d.%m.%Y %H:%M:%S")
print(formatted_date)

#3
five_date = "5 December, 2019"
five_object = datetime.strptime(five_date, "%d %B, %Y")
print(five_object)

#4
t1 = datetime.now()
t2 = datetime(2026, 1, 1)
print(t2 - t1)

#5
t1 = datetime.now()
t2_string = "1 January 1970"
t2_object = datetime.strptime(t2_string, "%d %B %Y")
# t2 = datetime(1970, 1, 1)
print(t1 - t2_object)

#6



