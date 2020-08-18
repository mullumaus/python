#输入两个链表，找出它们的第一个公共节点。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        a = headA
        b = headB
        while a or b:
            if not a:
                a  = headB
            if not b:
                b = headA
            if a == b:
                return a
            a = a.next
            b = b.next

