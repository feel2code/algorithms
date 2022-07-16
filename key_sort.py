def sorting(number, new_array):
    for i in range(number - 1):
        for j in range(0, number-i-1):
            var1 = new_array[j] + new_array[j+1]
            var2 = new_array[j + 1] + new_array[j]
            if var1 < var2:
                new_array[j], new_array[j+1] = new_array[j+1], new_array[j]
    print("".join(new_array))


if __name__ == '__main__':
    num = int(input())
    array = input().split(' ')
    sorting(num, array)
