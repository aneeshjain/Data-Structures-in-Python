from lifo_stack_linked_list import Stack



def infix_to_postfix(exp):
    stack = Stack()

    operators = ['+', '-', '*', '^']
    precedence = [1,1,2,3]
    result = []

    for char in exp:
        #print("At character: ", char)
        #print("Result",result)
        #print("Stack",stack.showStack())
        if char not in operators + ['(', ')'] :
            result.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                result.append(stack.pop())
            stack.pop()

        elif char in operators:
            if stack.isEmpty() or stack.peek() == '(' or (precedence[operators.index(char)] > precedence[operators.index(stack.peek())]):
                #print("here")
                stack.push(char)

            else:
                #print("Stack Peek: ", stack.peek())
                while stack.peek() in operators:
                    if (precedence[operators.index(stack.peek())] >= precedence[operators.index(char)]):
                        popped_value = stack.pop()
                        #rint("Popped Value: ", popped_value)
                        result.append(popped_value)
                stack.push(char)

    if stack.isEmpty():
        return result
    else: 
        while not stack.isEmpty():
            result.append(stack.pop())
        return result



exp = "a+b*(c^d-e)^(f+g*h)-i"

postfix = infix_to_postfix(exp)

print(''.join(postfix))