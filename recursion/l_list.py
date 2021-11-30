class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head: Node=None) -> None:
        self.head = head

    def l_print(self):
        l = []
        self.curr_node = self.head
        while self.curr_node != None:
            l.append(self.curr_node.data)
            if self.curr_node.next != None:
                self.curr_node = self.curr_node.next
            else:
                print("Done")
                break
        print(l)
    
    def reverseList(self, head=None): 
        if head == None or head.next == None:
            return head
   
        node = self.reverseList(head.next)
        head.next.next = head

        #If you dont delete previus head will still point to 2 and not None
        head.next = None
  
        #Will keep returning last element 
        return node

def mergeSort(A: Node=None, B: Node=None):
    if A == None:
        print(B.data)
        return B
    if B == None:
        print(A.data)
        return A

    if A.data < B.data:
        print(A.data)
        A.next = mergeSort(A.next, B)  
        return A
    
    if A.data > B.data:
        print( B.data)
        B.next = mergeSort(A, B.next)  
        return B



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4



l1 = Node(10)
l2 = Node(9)
l3 = Node(7)

l1.next = l2
l2.next = l3



l_list = LinkedList(head=n1)
l_list.l_print()

n = l_list.reverseList(head=l_list.head)
r_list = LinkedList(head=n)
r_list.l_print()




n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4

s_list = mergeSort(l1, n1)

#s_list.l_print()




