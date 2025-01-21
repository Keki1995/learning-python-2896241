# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

# import the HTMLParser module
# in Python 3 you need to import from html.parser
from html.parser import HTMLParser

paragraphs = 0

# create a subclass of HTMLParser and override the handler methods
# TL;DR this is basically creating a child class, with the parent class being HTMLParser
# Remember!!!
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # make sure to use the global keyword if you wanna reference vars OUTSIDE the local scope
        global paragraphs
        if tag == "p":
            paragraphs += 1
        
        print("Encountered a start tag:", tag)
        pos = self.getpos() # returns a tuple that indicates the line and character pos
        # \t means a tab
        print("\tAt line: ", pos[0], " position ", pos[1])

        # "magic" or dunder variables that have special meaning to python
        if attrs.__len__() > 0:
           print("\tAttributes:")
           for a in attrs:
               print("\t", a[0], "=", a[1])

    def handle_data(self, data):
        if (data.isspace()):
            return
        print("Encountered some text data:", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_comment(self, data):
        print("Encountered comment:", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    # open the sample HTML file and read it
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)
    
    print("Paragraph tags:", paragraphs)

if __name__ == "__main__":
    main()
  