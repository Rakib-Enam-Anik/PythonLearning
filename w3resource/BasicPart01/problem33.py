"""Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero."""

def sum_three(x,y,z):
    if  x==y or y==z or x==z:
        sum  = 0
    else:
        sum = x+y+z
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))