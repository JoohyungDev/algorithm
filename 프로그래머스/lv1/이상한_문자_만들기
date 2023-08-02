def solution(s):
    s = s.split(' ')   # 공백을 기준으로 리스트 만들기. 각 단어끼리 묶인다
    answer = []
    for i in range(0, len(s)):
        for j in range(0, len(s[i])):
            if j % 2 == 0:                     # 짝수 인덱스면 대문자
                answer.append(s[i][j].upper())
            else:
                answer.append(s[i][j].lower())
        answer.append(' ')    # 각 단어가 끝나면 공백으로 구분
    answer = ''.join(answer)  # join으로 문자열 합침
    return answer[:-1]