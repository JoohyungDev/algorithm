# https://100.pyalgo.co.kr/?page=66#


def solution(data):
    data = data[0]
    before, cnt = None, 0
    result = ""
    for i in data:
        if before:
            if before == i:
                cnt += 1
            else:
                result += before + str(cnt)
                cnt = 1
                before = i
        else:
            before = i
            cnt += 1
    result += before + str(cnt)
    return result
