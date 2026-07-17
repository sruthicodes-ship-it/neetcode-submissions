
class LinkedList:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            else:
                i += 1
                curr = curr.next
        
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = LinkedList(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = LinkedList(val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        new_node = LinkedList(val)
        i = 0
        if index == 0:
            self.addAtHead(val)
            return
            
        while curr:

            if i == index:
                new_node.prev =  curr.prev
                new_node.next = curr
                curr.prev.next = new_node
                curr.prev = new_node
                return
            else:
                i += 1
                curr = curr.next
        
        if i == index:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head

        while curr:
            if i == index:
                if curr.prev:
                    curr.prev.next = curr.next                    
                else:
                    self.head = curr.next
                
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev

                return True
            else:
                i += 1
                curr = curr.next

        return False


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)