# https://100.pyalgo.co.kr/?page=47#


def solution(data, idx=0):
    if idx >= len(data) or data[idx] is None:
        return 0
    else:
        left, right = 2 * idx + 1, 2 * idx + 2
        return max(solution(data, left), solution(data, right)) + 1
