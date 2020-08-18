
class Stack:
    def __init__(self):
        self.data =[]

    def add(self,n):
        self.data.append(n)

    def remove(self):
        return self.data.pop()

    def peek(self):
        if len(self.data) > 0:
            return True
        return False

    def printf(self):
        print(self.data)

def weave(s1, s2):
    s3 = Stack()
    while s1.peek() or s2.peek():
        if s1.peek():
            s3.add(s1.remove())
        if s2.peek():
            s3.add(s2.remove())
    return s3


if __name__ =="__main__":
    s1 = Stack()
    s2 = Stack()
    for i in range(10):
        s1.add(i)
    for i in range(20,33):
        s2.add(i)

    s3= weave(s1, s2)
    s1.printf()
    s2.printf()
    s3.printf()
