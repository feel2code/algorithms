# ID 69410269
def partition(participants, left, right):
    pivot = (participants[left])
    i = left + 1
    j = right - 1
    while True:
        if i <= j and participants[j] > pivot:
            j -= 1
        elif i <= j and participants[i] < pivot:
            i += 1
        elif (participants[j] > pivot) or (participants[i] < pivot):
            continue
        if i <= j:
            participants[i], participants[j] = participants[j], participants[i]
        else:
            participants[left], participants[j] = participants[j], participants[left]
            return j


def quick_sort(participants, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(participants)
    if (right - left) > 1:
        p = partition(participants, left, right)
        quick_sort(participants, left, p)
        quick_sort(participants, p + 1, right)


class Participant:
    def __init__(self, name, tasks_solved, fee):
        self.name = name
        self.tasks_solved = tasks_solved
        self.fee = fee

    def __ge__(self, other):
        return self.__gt__(other) or self == other

    def __le__(self, other):
        return self.__lt__(other) or self == other

    def __gt__(self, other):
        if self.tasks_solved != other.tasks_solved:
            return self.tasks_solved < other.tasks_solved
        if self.fee != other.fee:
            return self.fee > other.fee
        return self.name > other.name

    def __lt__(self, other):
        if self.tasks_solved != other.tasks_solved:
            return self.tasks_solved > other.tasks_solved
        if self.fee != other.fee:
            return self.fee < other.fee
        return self.name < other.name

    def __str__(self):
        return self.name


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    participants_count = int(reader.readline())
    participants = list()
    for _ in range(participants_count):
        name, tasks, fee = reader.readline().strip().split(' ')
        participants.append(Participant(name, int(tasks), int(fee)))
    reader.close()
    quick_sort(participants)
    print(*participants, sep='\n')
