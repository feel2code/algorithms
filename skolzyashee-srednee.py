length = 7
timeseries = [4, 3, 8, 1, 5, 6, 3]
K = 3
# length = int(input())
# timeseries = list(map(int, input().split()))
# K = int(input())

def moving_average(length, timeseries, K):
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)
    for i in range(0, length - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
    print(" ".join(map(str, result)))

moving_average(length, timeseries, K)
