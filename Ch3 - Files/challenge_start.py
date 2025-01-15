# Python code​​​​​​‌‌​​​‌‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌ below
# Use print("messages...") to debug your solution.

import os
from os import path

show_expected_result = False
show_hints = False

def file_info():
    # Your code goes here.
    # get file path of the folder
    totalsize = 0
    if path.exists("deps"):
        src = path.realpath("deps")
        for item in os.listdir(src):
            # split returns a list of splited substrings
            # [-1] means we only take the last element of that list (a single string var)
            # .lower makes it lowercase
            extension = item.split(".")[-1].lower()
            if extension == "txt":
                filepath = src + "/" + item
                totalsize = totalsize + os.path.getsize(filepath)

    # do a count of the files inside
    # do a for loop, checking if each file is a txt file
    # if so, add the file size to a additive counter
    
    return totalsize
