#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#

# TODO: import the calendar module
import calendar

# TODO: create a plain text calendar
# the .SUNDAY part specifies that we should start the week on sunday instead of monday, the default
c = calendar.TextCalendar(calendar.SUNDAY)
# formatmonth() turns the calendar object into a string that can be printed to look like a human-readable calendar
# arguments in sequence: year, month, width, length (width and length of the calendar)
str = c.formatmonth(2022, 1, 0, 0)
print(str)

# TODO: create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2022, 1)
print(str)

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month (go print it to see what this means)
for i in c.itermonthdays(2022, 8): # args: year, month
  print(i)
  
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
  print(name)

for day in calendar.day_name:
  print(day)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

print("Team meetings will be on:")
for m in range(1,13):
  # returns an array of weeks that represent the month
  cal = calendar.monthcalendar(2022, m)
  # The first Friday has to be within the first two weeks
  weekone = cal[0]
  weektwo = cal[1]

  #note: calendar.MONDAY to calendar.SUNDAY is literally just the integers 0-6
  if weekone[calendar.FRIDAY] != 0:
    meetday = weekone[calendar.FRIDAY]
  else:
    # if the first friday isn't in the first week, it must be in the second
    meetday = weektwo[calendar.FRIDAY]

  print("%10s %2d" % (calendar.month_name[m], meetday))