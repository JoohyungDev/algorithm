def solution(nums):
    answer = set(nums)
    
    if len(answer) > len(nums)/2:
        return len(nums)-len(nums)/2
    return len(answer)

# def solution(nums):
#     return min(len(set(nums)), len(nums)//2)