class Node:

    def __init__(self, d, n = None):
        self.data = d
        self.next = n
    
    def setData(self, d):
        self.data = d
    def getData(self):
        return self.data
    def setNext(self, n):
        self.next = n
    def getNext(self):
        return self.next
    
class Stack:

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def push(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def isEmpty(self):
        if self.root == None:
            return True
        else: return False

    def pop(self):
        if not self.isEmpty():
            popped_node = self.root    
            self.root = self.root.getNext()
            self.size -= 1
            return popped_node.getData()
        else:
            print("Stack Empty")

    def showStack(self):
        this_node = self.root
        while this_node:
            print(this_node.getData()) 
            this_node = this_node.getNext()
        
myStack = Stack()
print(myStack.isEmpty())

myStack.push(3)
myStack.push(2)
myStack.push(7)
myStack.push(6)
myStack.push(4)
myStack.showStack()
print(myStack.isEmpty())

popped_value = myStack.pop()
#print(popped_value)
myStack.showStack()


    
     

     