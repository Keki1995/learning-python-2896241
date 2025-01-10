#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#

# note that this is how python defines functions
# notice how python determines what belongs inside the function based on the indentation of the following lines
def main():
  print("Hello World!")
  name = input("WHat's your name?")
  print("Nice to meet you", name)

# TL;DR all python scripts have a secret var called __name__ for some goddamn reason
# when you run a script directly, this __name__ var is given the string "__main__" as its value
# so what we are doing is doing a check to see that this script is being run directly. If so, then run the main() function
if __name__ == "__main__":
    main()

# Note: when you import this script as a module in another Python file, this __name__ var is instead given the value of the module's name instead
# example, if the module is called time_controller, then the __name__ var will be given the value of "time_controller"