class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(-1)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            'None'

    def size(self):
        return len(self.items)


def is_correct_bracket_seq(seq):
    seq_stack = Stack()
    closed_brackets = ['()', '{}', '[]']
    opened_bracket = ['(', '{', '[']
    closed_bracket = [')', '}', ']']
    for i in seq:
        if i in opened_bracket:
            seq_stack.push(i)
        elif i in closed_bracket:
            bracket = seq_stack.peek()
            if (str(bracket) + i) in closed_brackets:
                seq_stack.pop()
            else:
                return False
    if seq_stack.size():
        return False
    return True


if __name__ == "__main__":
    sequence = input()
    print(is_correct_bracket_seq(sequence))
