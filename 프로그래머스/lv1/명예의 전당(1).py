def solution(k, score):
    answer = []
    mid = []   # 명예의 전당 저장 리스트
    
    for idx,i in enumerate(score):
        if idx+1 <= k:
            mid.append(i)
            answer.append(min(mid))
        else:
            if i > min(mid):
                mid.remove(min(mid))
                mid.append(i)
            answer.append(min(mid))

    return answer
