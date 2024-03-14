# https://100.pyalgo.co.kr/?page=64#


def solution(data):
    text, pattern = data
    count = start = 0
    while start < len(text):
        # 패턴이 존재하면 그 인덱스 반환
        pos = text.find(pattern, start)
        # 해당 패턴이 존재하면
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count
