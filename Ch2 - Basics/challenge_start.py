# Python code​​​​​​‌‌​​​‌‌‌​​‌‌‌‌​‌​​‌​​‌‌​​ below
# Use print("messages...") to debug your solution.
import string

show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # a translation table is made with the str.maketrans function, it tells python how to translate one char to another
    # this translation table is to be used with str.translate
    translation_table = str.maketrans('','',string.punctuation)
    # this is running 3 things on a string: casefold (turning all into lowercase), translation and replacement
    originalString = str.casefold(teststr).translate(translation_table).replace(" ","")
    # reversing the string
    reversedString = originalString[::-1]
    if reversedString == originalString:
        return True
    else:
        return False

# This is how your code will be called.
# Your function should return whether a string is a palindrome.
# The code will count the number of correct answers.
total = 0
test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.",
    "Race car!"]
for word in test_words:
    total += is_palindrome(word)

print(total)