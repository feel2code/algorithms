# ID 69379504
class Deck:
    def __init__(self, max_size: int):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x: int):
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            return 'error'

    def push_front(self, x: int):
        if self.size != self.max_size:
            self.queue[self.head - 1] = x
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            return 'error'

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return x


def main():
    commands_length = int(input())
    queue_length = int(input())
    queue = Deck(queue_length)
    for i in range(commands_length):
        command = input()
        operation, *value = command.split()
        if value:
            if operation == 'push_back':
                a = queue.push_back(int(*value))
                if a is not None:
                    print(a)
            if operation == 'push_front':
                a = queue.push_front(int(*value))
                if a is not None:
                    print(a)
        else:
            if operation == 'pop_front':
                print(queue.pop_front())
            if operation == 'pop_back':
                print(queue.pop_back())


if __name__ == '__main__':
    main()
