# https://100.pyalgo.co.kr/?page=67#


def solution(data):
    text, sub = data
    start_idx = 0
    result = []
    while start_idx != -1:
        start_idx = text.find(sub, start_idx)
        result.append(start_idx)
        start_idx += 1
    return result
