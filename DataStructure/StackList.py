
stack=[]
def push():
    element = input("Enter the element:")
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty!")
    else:
        e = stack.pop()
        print("removed element:", e)
        print(stack)
while True:
    print("Select the operation 1. push 2.pop 3.quit")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct operation!")