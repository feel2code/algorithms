n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = []
i = 0
while i < n:
    x.append(a[i])
    x.append(b[i])
    i += 1

print(" ".join(map(str, x)))
