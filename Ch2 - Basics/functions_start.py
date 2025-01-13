#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
  print("I am a function")

# TODO: function that takes arguments
def func2(arg1, arg2):
  print(arg1," ", arg2)

# TODO: function that returns a value
def cube(x):
  return x * x * x

# TODO: function with default value for an argument
def power(num, x=1):
  result = 1
  for i in range(x):
    result = result * num
  return result

# TODO: function with variable number of arguments
def multi_add(*args): # the * is a wildcard, allows us to specify any number of args
  result = 0
  for x in args:
    result = result + x
  return result

# this will print out:
# I am a function
func1()

# this will print out:
# I am a function
# None
print(func1()) # this is because func1 runs, executing its own print, then the print() function itself resolves, but since func1 has no return value it prints "None"

# this will print out:
# <function func1 at 0x0000027FE5F3A340>
print(func1) # this literally prints out the function definition, which is the funny string you see above. The above string is the function object itself

func2(10, 20)
print(func2(10, 20))
print(cube(3))

print(power(2))
print(power(2,3))
# note, Python allows you to supply argument values in any order if you do this below and name them
print(power(x=3, num=2))
# note, if you do want use the *arg for variable numbers of args, this has to be your last argument, you cannot mix it up like in the previous example
print(multi_add(4,5,10,4))