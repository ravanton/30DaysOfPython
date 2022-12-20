# Python datetime
# Python has got datetime module to handle date and time.

import datetime
print(dir(datetime))

# Getting datetime Information
# from datetime import datetime

# now = datetime.now()
# print(now)

# day = now.day                   
# month = now.month               
# year = now.year                 
# hour = now.hour                 
# minute = now.minute             
# second = now.second
# timestamp = now.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 9/12/2022, 20:8

# Difference Between Two Points in Time Using timedelata
# from datetime import timedelta
# t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
# t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
# t3 = t1 - t2
# print("t3 =", t3)

# Exercises 
# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print('timestamp', timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
t = now.strftime("%m/%d/%Y, %H:%M:%S") # mm/dd/YY H:M:S format
print(f"strftime format: {t}")

# Calculate the time difference between now and new year.
from datetime import date
today = date(year = 2022, month = 12, day = 20)
new_year = date(year = 2023, month = 1, day = 1)

time_left_for_newyear = new_year - today
print("Time left for New Year:", time_left_for_newyear)