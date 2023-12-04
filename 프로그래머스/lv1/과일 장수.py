def solution(k, m, score):
    answer = 0
    idx = 0
    box_list = []
    sorted_score = sorted(score, reverse=True)
    
    while idx+m <= len(sorted_score):
        for i in range(idx,idx+m):
                box_list.append(sorted_score[i])
                if len(box_list) == m:
                    answer += min(box_list)*m
                    box_list = []
                    idx += m
                
    return answer