""" Write a Python program to check whether a string is numeric."""
#Doesn't work for floats
text = input("Input a word or a number:")
if text.isdigit():
    print("The input value is number.")
else:
    print("The input value is string.")    