class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        i = 0
        cur = self.head
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return

        new_node = ListNode(val)

        # transverse to tail
        cur = self.head
        while cur:
            if not cur.next:
                break
            cur = cur.next
        
        # point current tail to new_node
        cur.next = new_node
        
        self.display()
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        # find the node before the given index
        cur = self.head
        pos_before_index = index - 1
        i = 0
        while cur:
            if i == pos_before_index:
                break
            cur = cur.next
            i += 1

        # cur is now the node before given index
        if not cur:
            return

        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return

        # find the node before the given index
        cur = self.head
        pos_before_index = index - 1
        i = 0
        while cur:
            if i == pos_before_index:
                break
            cur = cur.next
            i += 1

        # cur is now the node before given index
        if not cur:
            return
        
        if not cur.next: # The node we want to delete does not exist
            return

        cur.next = cur.next.next
        
    def display(self):
        cur =  self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)