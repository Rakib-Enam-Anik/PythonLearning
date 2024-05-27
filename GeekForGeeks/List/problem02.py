"""
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

Examples:  

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""

def swappositions(lis, pos1, pos2):
    temp = lis[pos1]
    lis[pos1] = lis[pos2]
    lis[pos2] = temp
    return lis

List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swappositions(List, pos1-1, pos2-1))