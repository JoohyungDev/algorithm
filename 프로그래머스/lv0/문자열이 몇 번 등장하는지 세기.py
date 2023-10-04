def solution(myString, pat):
    count = 0
    index = myString.find(pat)  # 처음으로 찾은 pat 문자열의 인덱스

    while index != -1:  # pat이 존재하면 
        count += 1
        index = myString.find(pat, index + 1)
        
    return count
