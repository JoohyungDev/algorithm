def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(2*i)
    return answer

# [num*2 for num in numbers]
# 표현식 for 항목 in 반복가능객체 if 조건문 -> 리스트 컴프리헨션