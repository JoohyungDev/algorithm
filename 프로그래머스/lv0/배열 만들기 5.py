def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        my_str = ''.join(map(str,list(map(int,intStrs[i][s:s+l]))))
        if int(my_str) > k :    answer.append(int(my_str))
    return answer
