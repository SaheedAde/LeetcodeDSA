```
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
def recurse(head: Optional[ListNode], prev_node: Optional[ListNode] = None) -> Optional[ListNode]:
if not head:
return prev_node
​
next_node = head.next
head.next = prev_node
prev_node = head
return rec(next_node, prev_node)
​
return recurse(head)
```