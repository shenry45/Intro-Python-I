"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

print(datetime.now().strftime('%B'))

user_input = input('What month and year? Please separate with comma.')
listed_input = user_input.split(' ')


def input_handler(*input):
    # check for no input
    if input[0] == '' and len(input) > 0:
        # print out current month
        calendar.prmonth(datetime.now().year, datetime.now().month)
    # check for month input only
    elif len(input) == 1:
        # print out requested month (int)
        calendar.prmonth(datetime.now().year, int(input[0]))
    # check for month and year input
    elif len(input) == 2:
        # print requested month in requested year
        calendar.prmonth(int(input[1]), int(input[0]))
    else:
        print('Please enter a valid input. [month as integer 1-12] [year]')

input_handler(*listed_input)
