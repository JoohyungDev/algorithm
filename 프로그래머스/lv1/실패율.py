def solution(N, stages):
    stage_count = [0] * (N+2)  # 각 스테이지에 멈춰있는 사용자 수를 저장할 리스트
    
    for stage in stages:
        stage_count[stage] += 1
    
    total_players = len(stages)  # 전체 플레이어 수
    failure_rates = []

    for i in range(1, N+1):
        if total_players == 0:  # 스테이지에 도달한 플레이어가 없는 경우 실패율은 0
            failure_rate = 0
        else:
            failure_rate = stage_count[i] / total_players  # 실패율 계산

        failure_rates.append((i, failure_rate))
        total_players -= stage_count[i]  # 다음 스테이지를 위해 현재 스테이지의 플레이어 수를 뺌

    # 실패율을 기준으로 내림차순 정렬하되, 실패율이 같은 경우 스테이지 번호가 작은 것이 먼저 오도록 함
    failure_rates.sort(key=lambda x: (-x[1], x[0]))

    return [stage for stage, _ in failure_rates]  # 스테이지 번호만 반환
