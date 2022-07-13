# ID 69379728
class Stack:
    def __init__(self):
        self.results = []
        self.size = 0

    def push(self, element):
        self.size += 1
        self.results.append(element)

    def pop(self):
        if self.size == 0:
            return 'error'
        self.size -= 1
        return self.results.pop()


if __name__ == '__main__':
    stack = Stack()
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x
    }
    inputs = input().split(' ')
    for operand in inputs:
        operation = operators.get(operand)
        if operation:
            calculated = operation(stack.pop(), stack.pop())
            stack.push(calculated)
        else:
            stack.push(int(operand))
    print(stack.pop())
