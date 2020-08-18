
class Queue:
    def __init__(self):
        self.data =[]

    def add(self,n):
        self.data.append(n)

    def remove(self):
        return self.data.pop(0)

    def peek(self):
        if len(self.data) > 0:
            return True
        return False

    def printf(self):
        print(self.data)

def weave(q1,q2):
    q3 = Queue()
    while q1.peek() or q2.peek():
        if q1.peek():
            q3.add(q1.remove())
        if q2.peek():
            q3.add(q2.remove())
    return q3


if __name__ =="__main__":
    q1 = Queue()
    q2 = Queue()
    for i in range(10):
        q1.add(i)
    for i in range(20,33):
        q2.add(i)
    q3= weave(q1,q2)
    q3.printf()
