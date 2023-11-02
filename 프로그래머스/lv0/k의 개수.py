def solution(i, j, k):
    count = 0

    for i in range(i,j+1):
        if str(i).count(str(k)) >= 1:
            count += str(i).count(str(k))
            
    return count

# def solution(i, j, k):
#     answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
#     return answer