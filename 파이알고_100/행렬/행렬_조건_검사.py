# https://100.pyalgo.co.kr/?page=57#


def solution(data):
    matrix, condition = data
    matrix = sum(matrix, [])
    for i in matrix:
        if i % condition != 0:
            return False
    return True


solution([[[2, 4, 6], [8, 10, 12]], 2])
