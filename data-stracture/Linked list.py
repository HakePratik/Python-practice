class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkfedList:
   def __init__(self):
           self.head = None
           self.n = 0

   def __len__(self):
             return self.n

   def insert_head(self, value):
        if not self.notinsert(value):
           new_node = Node(value)
           new_node.next = self.head
           self.head = new_node
        self.n += 1
   def notinsert (self, value):
        new_node = self.head
        while new_node:
            if new_node.data == value: 
               return True
            new_node = new_node.next
        return False   
        
   def delete(self, key):
       # if new_node != key:
         #   print ("node is not present in list")
        new_node = self.head
        # If the node to be deleted is the head
        if new_node and  new_node.data == key:
            self.head =  new_node.next
            return
        # Search for the node to be deleted
        prev = None
        while  new_node and  new_node.data != key:
            prev =  new_node
            new_node =  new_node.next
        if not  new_node:
            return print ("node is not present")

   def print(self):
        if self.head is None:
            print("list is empty")
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next     
        print("]")
     
                
L = LinkfedList()
L.insert_head(3)
L.insert_head(5)
L.insert_head(2)
L.insert_head()
L.delete(10)
len(L)
print("Length of the linked list:", len(L))
print("Elements of the linked list:",end="["), L.print()

