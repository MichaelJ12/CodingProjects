class Node:
    def __init__(self, data):
        self.data = data # assigns the given data to the node
        self.next = None # Intitialize the next attribute to null

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data) # Create new node
        new_node.next = self.head # next for new node becomes the current head 
        self.head = new_node # head now points to the new node
    
    def printList(self):
        temp = self.head # start from the head of the list
        while temp: # loops till the end of the list 
            print(temp.data,end=' ') # print the data in the current node
            temp = temp.next # move to the next node 
        print() # ensurese the output is followed by a empty line 

    def insertAtEnd(self, new_data):
        new_node = Node(new_data) # create new node
        if self.head is None:
            self.head = new_node # if the list is empty make the new node  the head
            return
        last = self.head
        while last.next: # otherwise traverse(search) the list to find the lasst node 
            last = last.next
        last.next = new_node # make the new node the nesxt node of the last node 

    def deleteFromBeginning(self):
        if self.head is None:
            return "this list is empty" # if the list is empty print this
        self.head = self.head.next # otherwise, remove the head by makiung hte next node the new head

    def deleteFromEnd(self):
        if self.head is None:
            return "this list is empty"
        if self.head.next is None: 
            self.head = None # if there is only oen node remove the head
            return
        temp = self.head
        while temp.next.next: # otherwise go to the second last node 
            temp = temp.next
        temp.next = None # remove the last node by setting the second last node to None 

    def search(self, value):
        current = self.head # start withg the head of the list
        position = 0 # coutner to keep track of the position
        while current: # traverese the list 
            if current.data == value: # compare the list's data to the search value
                return f"Value '{value}' found at posistion {position}"  # print the value if a match is found
            current = current.next 
            position += 1 
        return f"Value '{value}' not found in the list"    

if __name__ == '__main__':
    #create a new Lijnkedlist isntance 
    llist = LinkedList()

    # insert each letter at the beginneing usiung the method we created
    llist.insertAtBeginning('fox')
    llist.insertAtBeginning('brown')
    llist.insertAtBeginning('quick')
    llist.insertAtBeginning('the')

    #instert a word at the end 
    llist.insertAtEnd('jack')

    # print the list
    print("list before deletion:")
    llist.printList()

    # deletting the nodes from the begginening and end
    llist.deleteFromBeginning()
    llist.deleteFromEnd()

    # print the list 
    print("List after deletion:")
    llist.printList()

    # searching for the value 
    print(llist.search('quick'))
    print(llist.search('lazy'))