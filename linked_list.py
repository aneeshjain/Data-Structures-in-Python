
class Node:

    def __init__(self, d, n = None):
        self.data = d
        self.next = n

    def get_next(self):
        return self.next


    def set_next(self, n):
        self.next = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

class LinkedList:

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size
        

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root
        prev_node = None
        
        while this_node != None:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True

            else: 
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, data):

        this_node = self.root

        while this_node:

            if this_node.get_data() == data:
                print("Data Found")
                return True

            else:
                this_node = this_node.get_next()
        print("Data not found")
        return False

    def print_list(self):
        this_node = self.root
        while this_node:
            print(this_node.get_data())
            this_node = this_node.get_next()

myList = LinkedList()

myList.add(1)
myList.add(5)
myList.add(2)
myList.add(3)
size = myList.get_size()
print("size = ", size)
myList.remove(5)

myList.print_list()

