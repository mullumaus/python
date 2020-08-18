class Stack:
    def __init__(self):
        self.data =[]

    def add(self,n):
        self.data.append(n)

    def remove(self):
        if self.peek():
            return self.data.pop()
        return None

    def peek(self):
        if len(self.data) > 0:
            return True
        return False

    def printf(self):
        print(self.data)


class Queue :
    def __init__(self):
        self.sIn = Stack()
        self.sOut =Stack()

    def add(self,n):
        self.sIn.add(n)

    def remove(self):
        if self.sOut.peek() is False:
            while self.sIn.peek():
                self.sOut.add(self.sIn.remove())
        return self.sOut.remove()

    def printf(self):
        print("sIn {}",q.sIn.data)
        print("sOut {}",q.sOut.data)

    def peek(self):
        return self.sIn.peek() or self.sOut.peek()


if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.add(i)
    q.printf()
    while q.peek():
        q.remove()
        q.printf()


