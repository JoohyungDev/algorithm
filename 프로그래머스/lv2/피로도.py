from itertools import permutations

def solution(k, dungeons):
    # 던전은 하루에 한 번씩 탐험 가능. 최대한 많이 탐험하고 싶음
    # k = 현재 피로도, dungeons = [최소필요도, 소모 피로도]
    # 탐험할 수 있는 최대 던전 수 return
    # 던전의 개수(전체 리스트 길이)는 1~8
    # 각각의 리스트(던전)는 원소 2개
    # 최소 필요도 >= 소모피로도, 피로도는 1~1000
    # 서로 다른 던전의 피로도가 같을 수 있음

    answer = -1
    visited = 0
    
    for dungeon_permutations in permutations(dungeons):
        # have = 현재 피로도 / count = 경우의 수
        have, count = k, 0  
        # need = 최소 필요도 / cost = 소모피로도
        for need, cost in dungeon_permutations: 
            if have >= need and have >= cost:
                have -= cost
                count += 1
        visited = max(visited, count)
    answer = visited
    return answer
