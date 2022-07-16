def subseq(substring, line):
    position = -1
    for i in substring:
        position = line.find(i, position + 1)
        if position == - 1:
            return False
    return True


if __name__ == '__main__':
    substring = input()
    line = input()
    print(subseq(substring, line))
