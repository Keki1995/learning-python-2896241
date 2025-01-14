#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    myfile=open("textfile.txt", "w+")
    # the 2nd arg in the open() function is the open mode
    # w means we open the file for writing. note, it WILL DELETE ALL PREVIOUS DATA in the file
    # + means we create the file if it doesn't exist. Also means we are opening the file for updating
    
    # Open the file for appending text to the end
    # myfile=open("textfile.txt", "a+")

    # write some lines of data to the file
    for i in range(10):
        # basically, %d will be replaced by whatever is after the % sign
        # use %d for numbers and %s for strings
        # \r\n is carriage return + newline, though you could just \n\n
        myfile.write("This is line %d\r\n" % (i+1))
    
    # close the file when done
    myfile.close()
    
    # Open the file back up and read the contents
    # the mode being "r" means we are opening the file to read
    # note: if you put r+ you can both read and write
    # compared to w+, r+ requires that the file already exists, if not it will throw an error. w+ will create the file if it doesn't exist
    myfile = open("textfile.txt", "r")
    if myfile.mode == 'r':
        # contents = myfile.read()
        # print(contents)
        fl = myfile.readlines()
        for x in fl:
            print(x)
        
        # so what's the difference between read() and readlines()?
        # read() basically reads the whole file as a single string
        # readlines() loads up line by line and stores it as a list
    
if __name__ == "__main__":
    main()
