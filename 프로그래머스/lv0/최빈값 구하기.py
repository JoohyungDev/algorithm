from collections import Counter

def solution(array):
    counter = Counter(array)
    most_common = counter.most_common()  # 최빈값 리스트를 반환
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1
    return most_common[0][0]

# 카운터의 형태 : Counter({1:1,2:2,3:3}) -> 숫자:빈도수를 의미
# counter.most_common() -> [(1,1),(2,2),(3,3)] 즉, 튜플들의 리스트 형태
        