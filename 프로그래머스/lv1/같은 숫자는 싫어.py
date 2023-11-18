from collections import deque

def solution(arr):
    init = -1    # 반복문에서 숫자가 같은지 파악하기 위한 변수
    my_arr = deque()
    
    for idx,i in enumerate(arr):
        if i != init:
            my_arr.append(i)
            init = i
    return list(my_arr)
        