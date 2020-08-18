#输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        retList=[]
        if head is None:
            return []
        node = head
        while node is not None:
            retList.append(node.val)
            node = node.next
        retList = retList[::-1]
        return retList

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        node = head.next
        head.next = None
        while node is not None:
            tmp = node.next
            node.next = head
            head = node
            node = tmp
        return head
