def solution(s):
    s = list(s)
    s.sort(reverse=True)
    s="".join(s)
    return s

# return ''.join(sorted(s, reverse=True) 이렇게 1줄도 가능
# sorted를 사용하면 문자열이 자동으로 정렬된 리스트로 변환됨 
       