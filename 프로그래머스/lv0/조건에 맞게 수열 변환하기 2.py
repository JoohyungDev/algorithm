def solution(arr):
    result = []
    count = 0
    
    while arr != result:
        result = arr.copy()
        
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2 == 0:
                arr[i] /= 2
            elif arr[i]<50 and arr[i]%2 != 0:
                arr[i] = arr[i]*2 + 1
        count += 1
        
    return count-1
