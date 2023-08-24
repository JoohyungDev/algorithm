def solution(sides):
    side = sorted(sides)
    if side[0]+side[1] > side[2]:
        return 1
    else:
        return 2

# 삼각형이 되기 위한 조건2 : 세 변의 총합 - 최대 변 길이 > 최대 변 길이