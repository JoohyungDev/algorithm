# https://100.pyalgo.co.kr/?page=41#

def solution(data):
    result = []
    for i in data:
        if i in ['(', '[', '{']:
            result.append(i)
        else:
            last = result.pop()
            if (last == '(' and i == ')') or (last == '[' and i == ']') or (last == '{' and i == '}') :
                pass
            else:
                return False
    return len(result) == 0