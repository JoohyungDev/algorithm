# https://100.pyalgo.co.kr/?page=58#


def solution(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return "Error"
    # (*matrix) = [1, 2] [3, 4]
    # 행렬의 각 열을 묶음
    # zip(*matrix) = [(1, 3), (2, 4)]
    print(*matrix)
    return [list(reversed(row)) for row in zip(*matrix)]


solution([[1, 2], [3, 4]])  # [[3, 1], [4, 2]]
