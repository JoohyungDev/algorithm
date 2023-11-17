def solution(number):  
    answer = 0  # 경우의수 
    
    for i in range(0,len(number)-2):    # 첫 번째 학생 구하는 반복문
        for j in range(i+1,len(number)):  # 두번째 학생 구하는 반복
            for k in range(j+1,len(number)):    # 세번쨰 구하는 반복
                if number[i]+number[j]+number[k] == 0:
                    answer += 1
    return answer

# from itertools import combinations
# def solution (number):
#     cnt = 0
#     for i in combinations(number,3):
#         if sum(i) == 0:
#             cnt += 1
#     return cnt