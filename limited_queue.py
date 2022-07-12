class Queue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, boba):
        self.queue[self.tail] = boba
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        biba = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return biba

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        return self.size


if __name__ == '__main__':
    commands_length = int(input())
    queue_size = int(input())
    queue = Queue(max_size=queue_size)
    results = []
    for i in range(commands_length):
        command = input().split()
        if command[0] == 'push':
            if queue.size == queue.max_n:
                results.append('error')
            else:
                queue.push(command[1])
        elif command[0] == 'pop':
            results.append(queue.pop())
        elif command[0] == 'peek':
            results.append(queue.peek())
        elif command[0] == 'size':
            results.append(queue.size)

    for element in results:
        print(element)
