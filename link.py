
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self, head = None):
        self.head = head

    def insertFirst(self,data,next):
        node=Node(data=data,next=next)
        self.head = node

    def size(self):
        node = self.head
        count = 0
        while node :
            count = count +1
            node = node.next
        return count

    def getLast(self):
        node = self.head
        while node :
            if node.next is None:
                return node
            node = node.next
        return node


    def clear(self):
        self.head = None

    def removeFirst(self):
        if self.head is not None:
            self.head = self.head.next

    def removeLast(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        preNode = self.head
        preNode = self.head
        node = preNode.next
        while node.next :
            preNode = node
            node = node.next
        preNode.next = None


    def insertLast(self,data):
        newNode=Node(data=data)
        lastNode = self.getLast()
        if lastNode is None:
            self.head = newNode
            return
        lastNode.next = newNode

    def getAt(self,index):
        count = 0
        node = self.head
        while node is not None:
            if count == index:
                return node
            node = node.next
            count = count +1
        return None

    def removeAt(self,index):
        if index == 0:
            self.head = self.head.next
            return

        preNode = self.getAt(index - 1)
        if preNode is not None and preNode.next is not None:
            preNode.next = preNode.next.next

    def insertAt(self,data,index):
        newNode = Node(data, None)
        if self.head is None:
            self.head = newNode
            return
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        preNode = self.getAt(index-1)
        if preNode is None:
            self.insertLast(data)
            return
        newNode.next = preNode.next
        preNode.next = newNode

    def midPoint(self):
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next
        return slow

    def circular(self):
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return True
        return False
    
    # return the last nth node
    def fromLast(self, n):
        slow = self.head
        fast = self.head
        for i in range(n):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        return slow

    def printf(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

# if __name__ == "__main__":
#     link = linkedList()
#     link.insertLast(10)
#     link.printf()
#     link.insertFirst(1)
