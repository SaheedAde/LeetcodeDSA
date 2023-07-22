# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode() # answer -> head -> ... -> tail

        merged_tail = answer # running node
        while list1 and list2:
            if list1.val <= list2.val:
                merged_tail.next = list1
                list1 = list1.next
            else:
                merged_tail.next = list2
                list2 = list2.next
                
            merged_tail = merged_tail.next
            
        # If there's is remainder in list1 or list2, merge it with merged_tail
        if list1:
            merged_tail.next = list1
        if list2:
            merged_tail.next = list2
            
        return answer.next