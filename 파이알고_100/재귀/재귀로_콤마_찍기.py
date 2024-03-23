# https://100.pyalgo.co.kr/?page=96#


def solution(data):
    num_str = str(data)

    if len(num_str) <= 3:
        return num_str

    left_part = num_str[:-3]
    right_part = num_str[-3:]
    return solution(int(left_part)) + "," + right_part
