# https://100.pyalgo.co.kr/?page=81#


def solution(data):
    for idx, i in enumerate(data):
        if idx == len(data) // 2:
            return i
    return data


solution([1, 2, 3, 4, 5])
