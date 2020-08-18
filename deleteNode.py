# /*
# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
#
# 返回删除后的链表的头节点。
# */
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.val == val:
            head = head.next
            return head
        tmp = head
        while tmp.next is not None:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
                return head
            tmp = tmp.next
        return head
