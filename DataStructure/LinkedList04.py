def add_before(self,data,x):
    if self.head is None:
        print("Linked list is empty!")
        return
    if self.head.data == x:
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        return
    n = self.head
    while n.ref is not None:
        if n.ref.data ==x:
            break
        n = n.ref 
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref 
            n.ref = new_node
            
def delete_begin(self):
    if self.head is None:
        print("LL is empty so we can't delete nodes!")
    else:
        self.head = self.head.ref
        
            
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_before(20, 10)
LL1.print_LL()