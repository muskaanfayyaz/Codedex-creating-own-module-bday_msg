from datetime import date, datetime
import random
from bday_message import bday_messages

today = date.today()

# Define the birthday
birthday_month = 3
birthday_day = 14

# Check if the birthday for this year has already occurred
if (today.month, today.day) > (birthday_month, birthday_day):
    # If it has, set the next birthday to next year
    next_birthday = date(today.year + 1, birthday_month, birthday_day)
else:
    # If it hasn't, set the next birthday to this year
    next_birthday = date(today.year, birthday_month, birthday_day)

time_difference = next_birthday - today

days_away = time_difference.days

if (today == next_birthday):
    print(bday_messages.bday_messages)

else:
    print(f'My next birthday is {days_away} days away!')