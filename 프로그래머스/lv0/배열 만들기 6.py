def solution(arr):
    i = 0
    stk = []
    
    while len(arr) > i:
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            del stk[-1]
            i += 1
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    return stk if len(stk) != 0 else [-1]