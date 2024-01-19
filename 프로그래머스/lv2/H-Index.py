def solution(citations):
    answer = 0
    i = 0
    count  = 0
    citations.sort()
    
    while i != len(citations):
        if i < len(citations):
            tmp = citations[i]
        for j in citations:
            if j >= tmp:
                count += 1
        if count > answer:
            answer = min(count,tmp)
        count = 0
        i += 1

    return answer