# https://100.pyalgo.co.kr/?page=54#/


def solution(data):
    room, path = data
    # 로봇의 초기 위치
    x, y = 0, 0

    # 청소한 칸의 수 초기화
    cleaned = 0

    # 방향에 따른 움직임을 나타내는 딕셔너리
    direction = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    # 청소 시작
    # 처음 칸은 무조건 1
    if room[x][y] == 1:
        cleaned += 1
        room[x][y] = 0

    for move in path:
        # 이동할 좌표값
        dx, dy = direction[move]
        # 이동 후 현재 좌표값
        nx, ny = x + dx, y + dy

        # 범위를 벗어나지 않는지 확인
        if 0 <= nx < len(room) and 0 <= ny < len(room[0]):
            x, y = nx, ny
            # 청소가 필요한 칸인지 확인
            if room[x][y] == 1:
                cleaned += 1
                room[x][y] = 0

    return cleaned


solution(([[1, 1, 0, 0], [0, 1, 1, 1], [1, 0, 0, 1]], "RDDRUL"))
