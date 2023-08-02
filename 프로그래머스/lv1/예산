def solution(d, budget):
    d = sorted(d)
    sum = 0
    count = 0
    for i in range(0, len(d)):  
        sum += d[i]
        count += 1
        if sum > budget:
            count -= 1
            break
    return count