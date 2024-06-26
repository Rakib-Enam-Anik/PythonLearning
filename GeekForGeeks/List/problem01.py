"""
Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
"""

def swapList(newList):
    size = len(newList)
    
    #swapping
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp
    
    return newList

newList = [80, 35, 9, 56, 24]
print(swapList(newList))