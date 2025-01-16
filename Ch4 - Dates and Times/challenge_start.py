# Python code​​​​​​‌‌​​​‌‌‌‌​​‌‌‌​‌​​​​​​‌‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

import calendar

def count_days(year, month, whichday):
    # this gives us the calendar for a particular month of the specified year
    cal = calendar.monthcalendar(year, month)

    count = 0

    for week in cal:
        if week[whichday] != 0:
            count = count + 1

    return count
