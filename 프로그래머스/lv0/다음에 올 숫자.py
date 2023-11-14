def solution(common):
    # 리스트 길이
    length = len(common)
    
    # 공차
    d = common[1] - common[0]
    # 공비
    if common[0] == 0:
        r = 0
    else:
        r= common[1] / common[0]

    if common[0] + 2*d == common[2]:
        return common[0] + length*d
    else:
        return common[0]*(r**(length))
