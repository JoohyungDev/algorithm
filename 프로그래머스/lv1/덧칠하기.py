def solution(n, m, section):
    count = 1
    init = 0 # 맨 처음 값 저장
    
    for i in section:
        if init+(m-1) < i:
            init = i
            count += 1
            
    return count
