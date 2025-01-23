import themodule
# you can also do the below like JS, then use the as name as da wae instead
# import themodule as moduleberg

def main():
    themodule.saytheword("bob")
    themodule.saytheword("chad")
    themodule.saymyname()
    print("main's __name__ is: " + __name__)

if __name__ == "__main__":
    main()