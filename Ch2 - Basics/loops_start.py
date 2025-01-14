#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while(x < 5):
        print(x)
        x = x + 1

    # TODO: define a for loop
    for x in range(5,10): # note, range(x,y) is done as x(inclusive) to y(exclusive)
        print(x)

    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in days:
        print(d)


    # TODO: use the break and continue statements
    for x in range(5,10):
        # if x == 7:
        #     break
        if x % 2 == 0: # if it's an even number
            continue
        print(x)

    # TODO: using the enumerate() function to get index
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for x,y in enumerate(days): # enumerate returns a pair of values, the index as well as the value, so we need 2 vars . The first var is the numerator, the 2nd var is the value
        print(x,y)
    
  
if __name__ == "__main__":
    main()
