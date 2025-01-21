# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request

def main():
    #open a connection to a URL using urllib2
    # note, this is basically sending a GET request to the server
    webUrl = urllib.request.urlopen("Http://www.google.com")

    #get the result code and print it
    print("result code: ", webUrl.getcode())

    #read the data from the URL and print it
    data = webUrl.read()
    print(data)

if __name__ == "__main__":
    main()
