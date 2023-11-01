def solution(score):
    answer = []
    avg_list = []
      
    for i in score:
        avg_list.append((i[0]+i[1])/2)

    sorted_avg_list = sorted(avg_list,reverse=True)
     
    for i in avg_list:
        answer.append(sorted_avg_list.index(i)+1)
    
    return answer