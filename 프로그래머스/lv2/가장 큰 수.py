def solution(numbers):
    if numbers.count(0) == len(numbers):
        return '0'
    
    # 숫자를 문자열로 변환하고, 4자리 수로 확장하기 위해 최대 길이인 4자리까지 반복
    sorted_numbers = sorted(numbers, key=lambda x: (str(x) * 3)[:4], reverse=True)

    # 정렬된 숫자를 문자열로 결합하여 출력
    largest_number = ''.join(str(x) for x in sorted_numbers)
        
    return largest_number
