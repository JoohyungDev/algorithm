# https://100.pyalgo.co.kr/?page=89#


def solution(data):
    line1, line2 = data
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    # 기울기 계산
    m1 = (y2 - y1) / (x2 - x1) if x1 != x2 else float("inf")
    m2 = (y4 - y3) / (x4 - x3) if x3 != x4 else float("inf")

    # 기울기가 다르면 교차점 계산
    if m1 != m2:
        if x1 == x2:  # 선분1이 수직선인 경우
            x = x1
            y = m2 * (x - x3) + y3
        elif x3 == x4:  # 선분2가 수직선인 경우
            x = x3
            y = m1 * (x - x1) + y1
        else:  # 일반적인 경우
            x = (y3 - y1 + m1 * x1 - m2 * x3) / (m1 - m2)
            y = m1 * (x - x1) + y1

        # 교차점이 두 선분 위에 있는지 확인
        if (
            min(x1, x2) <= x <= max(x1, x2)
            and min(x3, x4) <= x <= max(x3, x4)
            and min(y1, y2) <= y <= max(y1, y2)
            and min(y3, y4) <= y <= max(y3, y4)
        ):
            return (int(x), int(y))

    # 기울기가 같으면 평행 선분 확인
    else:
        # 두 직선의 y절편 계산
        c1 = y1 - m1 * x1
        c2 = y3 - m2 * x3

        # 두 직선이 일치하는지 확인
        if c1 == c2:
            # 겹치는 구간 확인
            x_start = max(min(x1, x2), min(x3, x4))
            x_end = min(max(x1, x2), max(x3, x4))
            y_start = max(min(y1, y2), min(y3, y4))
            y_end = min(max(y1, y2), max(y3, y4))

            # 겹치는 구간이 있다면 시작점 반환
            if x_start <= x_end and y_start <= y_end:
                return (x_start, y_start)

    # 교차점이 없으면 (0, 0) 반환
    return (0, 0)


solution((((1, 1), (3, 3)), ((1, 3), (3, 1))))
