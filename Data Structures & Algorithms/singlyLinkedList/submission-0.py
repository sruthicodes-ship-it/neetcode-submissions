class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if index == i:
                return curr.val
            else:
                i += 1
                curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = self.tail =  new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0 
        curr =  self.head
        prev = None
        while curr:
            if i == index:
                if curr == self.head:
                    self.head = curr.next
                else:
                      prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev

                return True
            else:
                prev = curr
                curr = curr.next
                i += 1
        
        return False

    def getValues(self) -> List[int]:

        curr = self.head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
