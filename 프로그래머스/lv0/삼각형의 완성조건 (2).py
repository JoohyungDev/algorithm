def solution(sides):
    max_len = max(sides)
    min_len = min(sides)
    count = 0

    for i in range(1, max_len+min_len):
        if i == max(max_len, min_len, i):   # 나머지 한 변이 가장 크다면
            if i < max_len + min_len:
                count += 1
        if max_len == max(max_len, min_len, i):   # max_len이 가장 크다면
            if max_len < min_len + i:
                count += 1 

    return count-1