class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):

        if not head:
            return head
        # create copy
        nex = cur = head

        while cur:
            nex = cur.next
            c_n = Node(cur.val)
            cur.next = c_n
            c_n.next = nex
            cur = nex
        
        # random links
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # seprate links
        cur = head
        s_head = Node(0)
        dp = s_head
        while cur:
            nex = cur.next.next
            dp.next = cur.next
            cur.next = nex

            cur = cur.next
            dp = dp.next
        
        return s_head.next