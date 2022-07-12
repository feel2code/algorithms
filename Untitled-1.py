map_length = int(input())
house_map = list(map(int, input().split()))

range_num = 10 ** 9
result = [range_num] * map_length
greater = range_num
for i in range(map_length):
    if not house_map[i]:
        greater = 0
    result[i] = min(result[i], greater)
    greater += 1

greater = range_num
for i in range(map_length - 1, -1, -1):
    if not house_map[i]:
        greater = 0
    result[i] = min(result[i], greater)
    greater += 1
print (' '.join(map(str, result)))
