# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
print("\nBasic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries")
# these are numbers
myint = 5
myfloat = 13.2
# these are strings
mystr = "This is a string"
# these are bools
mybool = True
# these are sequences
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2) # tuples are immutable (cannot be changed once made) sequences of values
# these are dictionaries
mydict = {"one" : 1, "two" : 2} # "one" and "two" are the keys, and the values behind the ":" are the values associated with the keys

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
print("\nre-declaring a variable works")
myint = "abc"
# basically, you can change the value type in variables whenever you want
print(myint)

# to access a member of a sequence type, use []
print("\nto access a member of a sequence type, use []")
print(mylist[2])
print(mytuple[1])

# use slices to get parts of a sequence
print("\nuse slices to get parts of a sequence")
print(mylist[1:4]) # this means we look at the stuff in the list from index 1 (inclusive) to index 4 (EXclusive)
print(mylist[1:5:2]) # the same as above, but the extra :2 means that we are skipping every 2nd value, so every other value in this case

# you can use slices to reverse a sequence
print("\nyou can use slices to reverse a sequence")
print(mylist[::-1]) # using ":" without specifying a start and end index means we just take the whole thing, and "-1" means we reverse the sequence. The end result is that we print the whole thing in reverse

# dictionaries are accessed via keys
print("\ndictionaries are accessed via keys")
print(mydict["one"])

# ERROR: variables of different types cannot be combined
print("\nERROR: variables of different types cannot be combined")
print("make sure to concat stuff of the same type " + str(123)) # use stuff like the inbuilt str function to convert stuff to the same type, since Python is a strongly-typed language

# Global vs. local variables in functions
print("\nGlobal vs. local variables in functions")

def someFunction():
  mystr = "def"
  print(mystr)

someFunction() # prints local mystr
print(mystr) # prints global mystr

def someFunction2():
  global mystr # this tells the function to use the global mystr variable instead
  mystr = "def" # modifies the global mystr
  print(mystr)

someFunction2()
print(mystr) # prints the new value since we changed it inside someFunction2

del mystr # this deletes a previously defined variable. This means you can "undefine" stuff
print(mystr)