class MinStack:

    def __init__(self):
        self.stack = [] # list of tuple of value and min
        

    def push(self, val: int) -> None:
        if self.stack:
            current_min = min(self.getMin(), val)
            self.stack.append((val, current_min))
        else:
            self.stack.append((val, val))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()