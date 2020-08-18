

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

    def add(self,data):
        newNode = Node(data)
        self.children.append(newNode)
        return newNode

    def remove(self,val):
        for node in self.children:
            if node.data == val:
                self.children.remove(node)

    def printf(self):
        print("Parent:",self.data)
        for child in self.children:
            print(child.data)

#breadth first traverse: non recursive
def traverseBF(node):
    nodeList=[node]
    head = 0
    while head!=len(nodeList):
        if len(nodeList[head].children) > 0:
            nodeList.extend(nodeList[head].children)
        head = head +1
    for n in nodeList:
        print(n.data)

#breadth first traverse: recursive
def traverseBFRecursive(node, list):
    if node is not None and len(node.children) > 0:
        list.extend(node.children)

    for child in node.children:
        traverseBFRecursive(child,list)

#breadth first traverse: recursive
def traverseBFRec(root):
    list=[root]
    traverseBFRecursive(root,list)
    for node in list:
        print(node.data)

# breadth first traverse: recursive
def traserveDeepthRecursive(node,list):
    if node is not None:
        list.append(node)
    for child in node.children:
        traserveDeepthRecursive(child,list)

def traserveDeepthRecur(root):
    list=[]
    traserveDeepthRecursive(root,list)
    for node in list:
        print(node.data)
# breadth first traverse: non-recursive
#use a queue to store the node
def traserveDeepthNonRecursive(node):
    if node is None:
        return
    stack=[node]
    outList=[]
    while len(stack)>0:
        topNode=stack.pop()
        outList.append(topNode)
        for child in reversed(topNode.children):
            stack.append(child)
    for n in outList:
        print(n.data)


#get the tree level
def level(node):
    counter=[]
    nodelist = [node, None]
    pointer = 0
    while True:
        nodeCount = 0
        while nodelist[pointer] != None:
            if len(nodelist[pointer].children) >0:
                nodelist.extend(nodelist[pointer].children)
            nodeCount = nodeCount + 1
            pointer = pointer + 1
        counter.append(nodeCount)
        if pointer == len(nodelist) -1:
            break
        nodelist.append(None)
        pointer = pointer + 1


def generatorTree():
    root = Node(1)
    node1 = root.add(2)
    node2 = root.add(3)
    node1.add(21)
    node1.add(22)
    node1.add(23)

    node2.add(31)
    node2.add(32)
    return root



if __name__=="__main__":
    root =generatorTree()
    traserveDeepthNonRecursive(root)

