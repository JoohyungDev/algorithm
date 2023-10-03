def solution(myString, pat):
    myString = list(myString)  # 문자열을 리스트로 변환
    last_pat_index = 0
    result = []

    for i in range(len(myString)):
        result.append(myString[i])
        if ''.join(result).endswith(pat):
            last_pat_index = i
            
    return (''.join(myString))[:last_pat_index+1]

# def solution(myString, pat):
#     return myString[:len(myString) - myString[::-1].index(pat[::-1])]