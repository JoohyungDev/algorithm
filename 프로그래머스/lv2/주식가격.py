def solution(prices):
    answer = []
    seconds = 0
    
    for idx, i in enumerate(prices):
        seconds = 0
        for j in range(idx+1,len(prices)):
            seconds += 1
            if prices[idx] > prices[j]:   # 주식이 떨어지게 되면
                break
        answer.append(seconds)
    return answer