def solution(num):
    answer = []
    count = len(num)
    for i in range(0, count):
        for j in range(i+1, count):
            result=num[i]+num[j]
            answer.append(result)
    return sorted(list(set(answer)))