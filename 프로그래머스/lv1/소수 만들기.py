def solution(nums):
    answer = 0
    total = 0   # 각 자리 숫자의 합
    
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                total += nums[i]+nums[j]+nums[k]
                if total % 1 == 0 and total % total == 0:
                    answer += 1
                for x in range(2,total):
                    if total % x == 0:
                        answer -= 1
                        break
                total = 0
    return answer

# from itertools import combinations
# def prime_number(x):
#     answer = 0
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             answer+=1
#     return 1 if answer==1 else 0

# def solution(nums):
#     return sum([prime_number(sum(c)) for c in combinations(nums,3)])
