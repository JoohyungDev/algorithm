def solution(arr, flag):
    result = []
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(arr[i]*2):
                result.append(arr[i])
        elif flag[i] == False:
            for i in range(arr[i]):
                del result[-1]
    return result
            
# def solution(arr, flag):
#     arr1 = []
#     for i, j in zip(arr, flag):
#         if j:
#             arr1 += [i] * i * 2
#         else:
#             arr1 = arr1[:-i]
#     return arr1