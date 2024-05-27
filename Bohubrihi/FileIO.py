
def swaplist(newlist):
    newlist_length = len(newlist)
    
    
    tem = newlist[0]
    
    newlist[0] = newlist[newlist_length -1]
    newlist[newlist_length -1] = tem
    
    
    return newlist

newlist = [ 4, 5, 6, 7, 88]

print(swaplist(newlist))