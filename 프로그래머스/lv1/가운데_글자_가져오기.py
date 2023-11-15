def solution(s):
    if len(s) %2 == 0:
        return s[(len(s)//2)-1]+s[len(s)//2]
    else:
        return s[round(len(s)//2)]

# return str[(len(str)-1)//2:len(str)//2+1] 이런식으로 짧게도 가능
# 길이가 짝수든 홀수든 인덱스는 0부터 시작하기에 (전체길이 -1) // 2 하면  딱 중간 값이 나옴. 2:4 하면 4미만