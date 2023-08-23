def solution(n, k):
    # n= 인분, k = 음료수 개수, 총얼마를 지불하는가 return
    answer = 12000 * n + 2000 * k
    if n >= 10:
        answer -= 2000 * (n // 10)
    return answer