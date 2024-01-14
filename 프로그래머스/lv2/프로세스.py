from collections import deque

def solution(priorities, location):
    # (중요도, 인덱스) 튜플로 구성된 대기열 생성
    queue = deque((priority, idx) for idx, priority in enumerate(priorities))
    execution_order = 0
    
    while queue:
        # 현재 대기열에서 가장 우선순위가 높은 프로세스 찾기
        highest_priority = max(queue, key=lambda x: x[0])[0]
        current_item = queue.popleft()
        print(current_item)

        if current_item[0] < highest_priority:
            # 현재 아이템의 중요도가 가장 높지 않으면 대기열 끝으로 보내기
            queue.append(current_item)
        else:
            # 현재 프로세스 실행 (대기열에서 제거)
            execution_order += 1
            if current_item[1] == location:
                # 실행 순서가 궁금한 프로세스라면 실행 순서 반환
                return execution_order
