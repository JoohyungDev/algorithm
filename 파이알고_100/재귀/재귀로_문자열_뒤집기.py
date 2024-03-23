# https://100.pyalgo.co.kr/?page=95#


def solution(data):
    if len(data) <= 1:
        return data
    return data[-1] + solution(data[:-1])


solution("hello")
