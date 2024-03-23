# https://100.pyalgo.co.kr/?page=80#


def solution(data):
    max_distance = 0
    n = len(data)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = data[i]
            x2, y2 = data[j]
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            max_distance = max(max_distance, distance)

    return int(max_distance)
