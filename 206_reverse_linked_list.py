"""
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = head
        length = 0
        while(pre):
            length += 1
            pre = pre.next
   
        if length == n :
            return head.next
        else:
            cur = head
            for i in range(length - n-1):
                cur = cur.next
            cur.next = cur.next.next
        return head
    
    

    
    
    
