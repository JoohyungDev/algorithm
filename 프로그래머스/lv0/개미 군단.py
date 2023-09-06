def solution(hp):
    # 장군 개미는 5, 병정은 3, 일개미는 1.
    return hp//5+(hp%5)//3+hp%5%3

# def solution(hp):
#     answer = 0
#     for ant in [5, 3, 1]:
#         d, hp = divmod(hp, ant)
#         answer += d
#     return answer
