def solution(num, total):
    mid = total // num
    
    if num%2 != 0:
        init = mid - num//2
        return [i for i in range(init,init+num)]
    else:
        init = mid - (num//2-1)
        return [i for i in range(init,init+num)]
