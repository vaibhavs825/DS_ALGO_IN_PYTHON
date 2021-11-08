class Node:
    def __init__(self,data=None):
        if(data==None):
            self.data = None
        self.data = data
        self.next = None

def length(l):
    len = 0
    while(l != None):
        len += 1
        l = l.next
    return len

a = Node(1)
b = Node(2)
c = Node(8)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e

p = Node(4)
q = Node(5)
p.next = q
q.next = c


def merge(l1,l2):
    len1 = length(l1)
    len2 = length(l2)
    p = l1
    q = l2
    if (len1>len2):
        diff = len1-len2
        while(diff>0):
            p = p.next
            diff -= 1
    else:
        diff = len2-len1
        while(diff>0):
            q = q.next
            diff -= 1

    while(p!=None and q!=None):
        if(p==q):
            return p.data
        p = p.next
        q = q.next

    return -1

print(merge(p,a))


