# Learning Linked Lists

# To start we will create a singly linked list to visualize the flow of data.
#
# We first need to start with a Node class to represent each data point.

class Node:
    def __init__(self, data = None, next = None):
        
        # data represents the actual data point we
        # will be inserting, can be any data type.
        self.data = data

        # next represents the next element in the
        # linked list
        self.next = next

class LinkedList:
    def __init__(self):

        # self.head represents the root (head) of our
        # linked list. It is initialized to None because
        # we have not specified what data will go here yet.
        self.head = None
    
    # Insert data at beginning of linked list
    def insert_beginning(self, data):

        # Initializing head node to a Node() object.
        #
        # Set the data to whatever the value passed in is,
        # and set the next node to None.
        self.head = Node(data, None)

    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return
        
        # Initialize placeholder variable 'elem' to the head node.
        #
        # This essentially makes:
        #   elem = Node(data, next)
        elem = self.head

        # While the next node is not None, iterate through the
        # linked list by setting elem to the value elem is
        # pointing to.
        while elem.next:
            elem = elem.next
        
        # Once we get to the end of the linked list, we set elem's
        # next value to be the value we have input.
        elem.next = Node(data, None)
        
    # Insert the value of a given index
    def insert_at_index(self, index, data):

        # First, a catch to make sure the index provided is in
        # the linked list.
        if index >= self.length() or index < 0:
            raise Exception("Invalid index.")
        
        # If the index provided is 0, run the insert_beginning()
        # method.
        if index == 0:
            self.insert_beginning(data)
            return

       # Set count to 0 and elem variable to the head node. 
        count = 0
        elem = self.head

        # While elem is not None, iterate through linked
        # list.
        while elem:

            # If count is equal to the provided index minus
            # 1.
            if count == index - 1:

                # A new Node object will be created with the value
                # provided and the 'next' variable pointing to the 
                # next element in the linked list.
                #
                # So, say we have a linked list like this:
                #
                #       16 -> 9 -> 23 -> None
                #
                # and we provide: insert_at_index(1, 5),
                # this means we want 16 to point at 5 and 5 to point
                # at 9.
                # Since 9 right now equals the next element and, therefore,
                # elem.next, we will set that equal to the 'next'
                # variable in a new Node object.
                node = Node(data, elem.next)

                # We then set this new node object equal to elem.next
                # then break out of the loop to finish.
                elem.next = node
                break
            
            # If we have not founf the required position yet, iterate
            # the count by 1 and set elem to the next element.
            count += 1
            elem = elem.next
    
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def remove(self, index):
        if index >= self.length() or index < 0:
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        elem = self.head
        while elem:
            if count == index - 1:
                elem.next = elem.next.next
                break
            count += 1
            elem = elem.next
    
    def print_llist(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        llist = ''
        elem = self.head
        while elem:
            llist += str(elem.data) + ' ---> '
            elem = elem.next
            if elem is None:
                llist += 'None'
        print(llist)


if __name__ == '__main__':

    llist = LinkedList()
    
    # llist.insert_beginning(2)
    llist.insert_end(14)
    llist.insert_end(35)
    
    llist.print_llist()
    # print(llist.length())
    
    llist.insert_at_index(1, 27)
    
    llist.print_llist()
    # print(llist.length())
