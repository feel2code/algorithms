class Stack:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(int(item))
        if not self.max_items:
            self.max_items.append(int(item))
        else:
            if int(item) > self.max_items[-1]:
                self.max_items.append(int(item))
            else:
                self.max_items.append(self.max_items[-1])

    def pop(self):
        self.items.pop()
        self.max_items.pop()

    def get_max(self):
        if not self.items:
            return None
        else:
            return self.max_items[-1]


if __name__ == '__main__':
    stack = Stack()
    n = int(input())
    result = []
    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            stack.push(command[1])
        elif command[0] == 'pop':
            if stack.get_max() is None:
                result.append('error')
            else:
                stack.pop()
        elif command[0] == 'get_max':
            result.append(stack.get_max())

    for x in result:
        print(x)
