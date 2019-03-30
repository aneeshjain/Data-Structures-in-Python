
def buildStack():
    stack = []
    return stack

def push(stack, data):

    stack.append(data)
    print("{} Succesfully pushed to top of stack".format(data))

def isEmpty(stack):
    if len(stack) == 0:
        return True
    else: return False

def pop(stack):
    if isEmpty(stack):
        return None
    print("Top of stack popped")
    return stack.pop()

def showStack(stack):
    for x in stack:
        print(x)

myStack = buildStack()
print(isEmpty(myStack))
push(myStack, 1)
push(myStack, 9)
push(myStack, 7)
push(myStack, 3)
push(myStack, 6)

print(isEmpty(myStack))
showStack(myStack)

pop(myStack)
showStack(myStack)