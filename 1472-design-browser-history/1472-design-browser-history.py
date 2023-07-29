class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        
    def append(self, val):
        new_node = ListNode(val)
        if not self.tail:
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


class BrowserHistory(DoublyLinkedList):

    def __init__(self, homepage: str):
        super().__init__()
        self.append(homepage)
        self.curr = self.tail

    def visit(self, url: str) -> None:
        self.tail = self.curr
        self.append(url)
        self.curr = self.tail

    def back(self, steps: int) -> str:
        i = 0
        curr = self.curr
        while curr and curr.prev:
            if i == steps:
                break
            curr = curr.prev
            i += 1
        
        # Curr is now the node of history backward
        self.curr = curr
        return curr.val

    def forward(self, steps: int) -> str:
        i = 0
        curr = self.curr
        while curr and curr.next:
            if i == steps:
                break
            curr = curr.next
            i += 1
        
        # Curr is now the node of history forward
        self.curr = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)