# https://100.pyalgo.co.kr/?page=91#


def solution(data):
    if data == 0:
        return 1
    return data * solution(data - 1)


solution(5)
