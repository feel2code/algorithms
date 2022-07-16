def bubble(length: int, array: list):
    sort1 = False
    while True:
        sort2 = False
        for i in range(length - 1):
            if int(array[i]) > int(array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                sort2 = True
                sort1 = True
        if sort2:
            print(' '.join(array))
        else:
            break
    if not sort1:
        print(' '.join(array))


if __name__ == '__main__':
    input_length = int(input())
    arr = input().split(' ')
    bubble(input_length, arr)
