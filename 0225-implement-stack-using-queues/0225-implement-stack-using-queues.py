class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # Real Q don't have pop, we can only dequeue from the left.
        # Using self.queue.pop robs us of the message of this task
        # return self.queue.pop()
        q_vals = list(self.q)
        q_vals.reverse()
        rev_q = deque(q_vals)
        popped_val = rev_q.popleft()

        rev_q_vals = list(rev_q)
        rev_q_vals.reverse()
        self.q = deque(rev_q_vals)
        
        return popped_val
        

    def top(self) -> int:
        return self.q[-1]
        
    def empty(self) -> bool:
        return not bool(len(self.q))
        
        
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()