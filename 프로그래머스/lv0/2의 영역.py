def solution(arr):
    if 2 not in arr:
        return [-1]
    else:
        indexes = []
        for i, value in enumerate(arr):
            if value == 2:
                indexes.append(i)
        if len(indexes) == 1:
            return [arr[indexes[0]]]
        else:
            for j in indexes:
                if j == indexes[0]:
                    init = j
                elif j == indexes[-1]:
                    end = j
            return arr[init:end+1]
            
# def solution(arr):
#     if 2 not in arr:
#         return [-1]
#     return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
