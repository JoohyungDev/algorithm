# https://100.pyalgo.co.kr/?page=100#


def solution(data):
    result = ""
    for idx, i in enumerate(data):
        if i.isdigit():
            result += data[idx - 1] * int(i)
    return result


solution("a3b2c1")
