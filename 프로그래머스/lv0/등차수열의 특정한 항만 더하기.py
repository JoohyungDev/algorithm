def solution(a, d, included):
    # a+(n-1)d
    # included[i] == i+1항
    # 1항부터 n항까지 true인 항만 더한 값 return
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a+i*d
    return answer
    
# def solution(a, d, included):
#     return sum((a + i * d) for i, inc in enumerate(included) if inc)
