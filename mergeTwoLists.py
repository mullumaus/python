#输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        n1 = l1
        n2 = l2
        if n1.val > n2.val:
            head = n2
            n2 = n2.next
        else:
            head = n1
            n1 = n1.next
        node = head
        while n1 is not None and n2 is not None:
            if n1.val < n2.val:
                tmp = n1.next
                node.next = n1
                n1 = tmp
            else:
                tmp = n2.next
                node.next = n2
                n2 = tmp
            if node.next is not None:
                node = node.next
        if n1.next is not None:
            node.next = n1
        if n2.next is not None:
            node.next = n2
        return head
