def solution(my_string):
    digits_sum = 0  # 초기화
    # 문자열 내의 숫자들을 분리하고 합산
    digits_sum = sum(int(digit) for digit in my_string if digit.isdigit())
    return digits_sum