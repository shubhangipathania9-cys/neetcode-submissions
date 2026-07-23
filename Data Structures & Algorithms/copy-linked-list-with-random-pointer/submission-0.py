"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        x={None:None}
        dummy= Node(0,head)
        curr = head
        while curr:
           copy=Node(curr.val)
           x[curr]=copy
           curr=curr.next
        curr=head
        while curr:
            copy=x[curr]
            copy.next = x[curr.next]
            copy.random =x[curr.random]
            curr=curr.next
        return x[head]
        


        