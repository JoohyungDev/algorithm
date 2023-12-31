from collections import deque

def solution(s):
    test = deque()
    
    for i in s:
        if i == '(':
            test.append(i)
        elif test:
            test.pop()
        else:
            return False
    if test:
        return False

    return True
