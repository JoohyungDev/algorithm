# 정수 idx가 주어졌을 때, idx <= i 이면서 arr[i] = 1 인 가장 작은 i의 값을 찾아서 
# 반환하는 solution 함수를 완성해 주세요. 단, 만약 그러한 i가 없다면 -1을 반환합니다.

def solution(arr, idx):
    for i in range(len(arr)):
        if i >= idx and arr[i] == 1:
            return i
        
    return -1

# def solution(arr, idx):
#     answer = 0
#     try:
#         answer = arr.index(1, idx)
#     except:
#         answer = -1

#     return answer
