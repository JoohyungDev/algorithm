def solution(n):
    count = 0
    for i in range(n):
        if i == 0:
            pass
        elif n % i == 0:
            count += 1
    return count+1