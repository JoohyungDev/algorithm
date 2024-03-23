# https://100.pyalgo.co.kr/?page=92#


def solution(data):
    if data == 0:
        return 0
    elif data == 1:
        return 1
    return solution(data - 1) + solution(data - 2)


solution(5)
