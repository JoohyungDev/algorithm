# https://100.pyalgo.co.kr/?page=94#


def solution(data):
    a, b = data
    if b == 0:
        return a
    else:
        return solution((b, a % b))


solution((24, 18))
