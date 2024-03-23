# https://100.pyalgo.co.kr/?page=79#


def solution(data):
    x, y = list(zip(*data))
    # [(0, 3, 0, 3, 1), (0, 0, 2, 2, 1)]
    cnt_x = [i for i in x if x.count(i) == 2]
    cnt_y = [i for i in y if y.count(i) == 2]
    if len(cnt_x) != 4 or len(cnt_y) != 4:
        return 0

    x1, x2 = min(cnt_x), max(cnt_x)
    y1, y2 = min(cnt_y), max(cnt_y)

    return abs(x2 - x1) * abs(y2 - y1)


solution([(0, 0), (3, 0), (0, 2), (3, 2), (1, 1)])
