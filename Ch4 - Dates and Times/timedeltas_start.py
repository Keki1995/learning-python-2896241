#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it
# think of this as just an object representing a certain amount of time
# you can use it in math-y ways, like adding or subtracting from datetime objects to give a resultant time
print(timedelta(days=365, hours=5, minutes=1))

# TODO: print today's date
now = datetime.now()
print("today is: " + str(now))

# TODO: print today's date one year from now
print("one year from now it will be: " + str(now + timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
print("in two weeks and 3 days it will be: " + str(now + timedelta(weeks = 2, days = 3)))

# TODO: calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks = 1)
# %A - Day of the week %B - Month of the year, %d - day number, %Y - Year number
s = t.strftime("%A %B %d, %Y")
print("one week ago it was " + s)

### How many days until April Fools' Day?

today = date.today() # get today's date
afd = date(today.year, 4, 1) # get April Fool's for the same year

# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April fools day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year = today.year + 1) # if so, get the date for the next year

# TODO: Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print("It's just", time_to_afd.days, "days until next April Fools' Day!")

