# https://100.pyalgo.co.kr/?page=93#


def solution(data):
    if len(data) == 1:
        return data[0]
    return data[0] + solution(data[1:])


solution([1, 2, 3, 4, 5])
