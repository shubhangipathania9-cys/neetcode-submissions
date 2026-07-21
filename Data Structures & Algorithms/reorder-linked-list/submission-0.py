# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        sec=slow.next
        prv = slow.next = None
        while sec:
            nxt=sec.next
            sec.next=prv
            prv=sec
            sec=nxt
        
        first,sec=head,prv
        while sec:
            tmp1,tmp2=first.next,sec.next
            first.next=sec
            sec.next=tmp1
            first,sec=tmp1,tmp2




