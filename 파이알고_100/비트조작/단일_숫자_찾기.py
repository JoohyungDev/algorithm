# https://100.pyalgo.co.kr/?page=29#

# def solution(data):
#     from collections import Counter
#     count = Counter(data)
#     # get은 주어진 키에 대한 값을 반환
#     return min(count.keys(), key=count.get)

# 정석 풀이
# ^= -> xor 연산(이진수 단위로 연산)
# 이진수로 바꾼 숫자의 같은 자리의 비트가 다르면 1
# 이진수로 바꾼 숫자의 같은 자리의 비트가 같으면 0
def solution(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# data = [4, 1, 2, 1, 2]
# 초기 상태: result = 0
# 첫 번째 요소(4)와 XOR 연산: result = 0(000) XOR 4(100) = 4(100)
# 두 번째 요소(1)와 XOR 연산: result = 4(100) XOR 1(001) = 5(101)
# 세 번째 요소(2)와 XOR 연산: result = 5(101) XOR 2(010) = 7(111)
# 네 번째 요소(1)와 XOR 연산: result = 7(111) XOR 1(001) = 6(110)
# 다섯 번째 요소(2)와 XOR 연산: result = 6(110) XOR 2(010) = 4(100)