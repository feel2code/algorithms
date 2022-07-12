# ID 69073175


def distance_to_house(house_map: list, map_length: int, range_num: int):
    """Find distance to nearest zero."""
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
    return ' '.join(map(str, result))


if __name__ == '__main__':
    range_num = 10 ** 9
    house_map = list(map(int, input().split()))
    map_length = int(input())
    print(distance_to_house(house_map, map_length, range_num))
