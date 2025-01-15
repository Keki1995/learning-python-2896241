#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
# we don't strictly have to import path, but it means that when we call path, we have to do os.path.getmtime() instead of just path.getmtime()
from os import path
import datetime
from datetime import date, time, timedelta
# this is a different time module, the below one is the standard time library module, while the above is part of the datetime module
import time


def main():
    # Print the name of the OS
    print(os.name)
    
    # Check for item existence and type
    print("Item exists: " + str(path.exists("textfile.txt"))) # typecast to string
    print("Item is a file: " + str(path.isfile("textfile.txt")))
    print("Item is a directory: " + str(path.isdir("textfile.txt")))
    
    # Work with file paths
    print("Item's path: " + str(path.realpath("textfile.txt"))) # displays full filepath
    print("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))
    # path.split makes a tuple with 2 entries: everything before the final slash, and the thing after the final slash (normally the filename)
    print(path.split(path.realpath("textfile.txt"))[0]) # use this to see each entry in the tuple
    
    # Get the modification time
    # path.getmtime gets the last modified time of a file in epoch time
    # time.ctime converts the funny number of epoch time into human readable time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    # the datetime module has a datetime class inside it, hence this weird double datetime thingy
    # essentially another way of showing the last modified time
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")
  
if __name__ == "__main__":
    main()
