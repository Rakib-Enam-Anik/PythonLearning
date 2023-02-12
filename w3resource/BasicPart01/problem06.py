"""Write a Python program that accepts a sequence of comma-separated numbers from the user and 
generates a list and a tuple of those numbers. """

values = input ("Input some comma seperated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)