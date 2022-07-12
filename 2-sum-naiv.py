a = int(input())
b = list(map(int, input().split()))
x = int(input())

def sum_2(a, b, x):
    for i in range(0, a):
        for j in range(i+1, a):
            if b[i] + b[j] == x:
                arr = [b[i], b[j]]
                return " ".join(map(str, arr))
    return None

print(sum_2(a, b, x))
