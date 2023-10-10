def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        arr1_total = sum(arr1)
        arr2_total = sum(arr2)
        
        if arr1_total == arr2_total:
            return 0
        else:
            return -1  if arr2_total > arr1_total else 1
    else:
        return -1 if len(arr2) > len(arr1) else 1

# def solution(arr1, arr2):
#     return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))
