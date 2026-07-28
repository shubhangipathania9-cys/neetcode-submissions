# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        g=dummy
        while True:
            Kth=self.getKth(g,k)
            if not Kth:
                break
            go=Kth.next
            prev , curr = Kth.next , g.next
            while curr != go:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            
            tmp=g.next
            g.next=Kth
            g=tmp
        return dummy.next

    def getKth(self , curr , k):
        while curr and k > 0:
            curr=curr.next
            k-=1
        return curr