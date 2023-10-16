def solution(n):
    result = []
    
    for i in range(n):
        result.append([])
        for j in range(n):
            if j == i:
                result[i].append(1)
            else:
                result[i].append(0)
    return result

# import numpy as np

# def solution(n):
#     return np.eye(n).tolist()