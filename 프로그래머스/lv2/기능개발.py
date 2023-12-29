import math

def solution(progresses, speeds):
    # 각 작업이 완료되는 데 필요한 날짜 계산
    days_left = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    answer = []
    max_day = days_left[0]  # 첫 번째 작업이 완료되는 날짜
    
    count = 1
    for day in days_left[1:]:
        if day <= max_day:  # 이전 작업과 같이 배포할 수 있는 경우
            count += 1
        else:  # 이전 작업보다 더 오래 걸리는 작업인 경우
            answer.append(count)
            count = 1
            max_day = day
            
    # 마지막 배포 날짜에 배포되는 작업 수 추가
    answer.append(count)
    
    return answer

