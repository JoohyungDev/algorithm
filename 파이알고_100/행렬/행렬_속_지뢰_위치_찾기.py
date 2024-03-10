# https://100.pyalgo.co.kr/?page=56#


def solution(data):
    mines = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 1:
                mines.append((i, j))
    return mines


solution([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
