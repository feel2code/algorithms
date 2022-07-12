a = int(input())
b = list(map(int, input().split()))
x = int(input())

def s2_sum(a, b, x):
    b.sort()
    left = 0
    right = a - 1
    while left < right:
        current_sum = b[left] + b[right]
        if current_sum == x:
            arr = [b[left], b[right]]
            return " ".join(map(str, arr))
        if current_sum < x:
            left += 1
        else:
            right -= 1
    return None

print(s2_sum(a, b, x))
