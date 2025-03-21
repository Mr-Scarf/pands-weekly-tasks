# weekday.py

# Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
# You will need to search the web to find how you work out what day it is.

# Author: David Scally

import datetime # Import datetime module

weekend = ('Saturday', 'Sunday') # Tuple of weekend days

today_time = datetime.datetime.now() # Returns current date & time.

day_of_week = today_time.strftime("%A")# Returns current day of the week

if day_of_week in weekend: # Check if current day is in weekend.
    print('It is the weekend, yay!')
else: # Check if not weekend day. Only choice of weekend or weekday so tuple for weekday not required for check, else statement used to capture any input outside of if condition.
    print('Yes, unfortunately today is a weekday')


#Source https://pynative.com/python-get-the-day-of-week/
#Source https://www.w3schools.com/python/python_datetime.asp