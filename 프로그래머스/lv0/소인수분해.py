def solution(n):
    answer = []
    # 2로 나눌 수 있는 만큼 나누기
    while n % 2 == 0:
        answer.append(2)
        n = n // 2
    # 3부터 홀수 소수로 나누기
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            answer.append(i)
            n = n // i
    # n이 2 이상이면 남은 수도 소인수로 추가(소수인 경우도 해당)
    if n > 2:
        answer.append(n)
    return sorted(list(set(answer)))
