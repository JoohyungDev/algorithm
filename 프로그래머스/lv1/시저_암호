def solution(s, n):
    if s == ' ':
        return s
    s = list(s)
    answer = []
    for i in range(len(s)):
        result = chr(ord(s[i]) + n)   # chr= 문자로 변환/ ord = 아스키코드로 변환
        if 65 <= ord(s[i]) <90 and 90 < ord(result):
            answer.append(chr(65+(ord(result)-91)))
        elif chr(122) < result:
            answer.append(chr(ord(result)-122+96))
        elif s[i] == ' ':
            answer.append(' ')
        elif s[i] == chr(90):            # Z
            answer.append(chr(65+n-1))      # A
        elif s[i] == chr(122):            # z
            answer.append(chr(97+n-1))    # a
        else:
            answer.append(result)
    return "".join(answer)


print(solution("AaZz", 25)) #ZzYy
print(solution("a  b", 1)) # "b     c" (O)  "b c" (X)  
print(solution("a b ", 1)) # "b c "
print(solution("P", 15))  # E
print(solution("B", 25))  # A
print(solution("D", 25))  # C

# 다음의 예제처럼 간단히 나타낼 수도 있음
# def caesar(s, n):
#     s = list(s)                                               문자열 s가 zz이런식으로 2개올경우 배열 선언이 없으면 오류뜸
#     for i in range(len(s)):                                   보내준 문자열 길이만큼 반복
#         if s[i].isupper():                                    문자열이 전부 대문자인지? 대문자면 true
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))     배열의 원소 = 아스키코드->문자로 변환((원소의 아스키코드 - A의 아스키코드값 + n(얼만큼 밀건지))%26(영어알파벳갯수)+A의아스키코드값)))
#         elif s[i].islower():                                  문자열이 전부 소문자인지?
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
#     return "".join(s)                                         배열을 ""을 기준으로 합친다