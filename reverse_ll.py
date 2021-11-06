class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        p = self.head
        q = None
        while(p != None):
            r = p.next
            p.next = q
            q = p
            p = r
        self.head = q


    def print(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next




ll = LinkedList()

first = Node(1)
second = Node(2)
third = Node(3)
ll.head = first
first.next = second
second.next = third

ll.print()

ll.reverse()

ll.print()



