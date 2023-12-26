def solution(clothes):
    category_count = {} # 각 카테고리의 등장횟수
    
    for item in clothes:
        category = item[-1]  # 카테고리는 각 원소의 마지막 항목
        
        if category in category_count:
            category_count[category] += 1  # 만약 해당 카테고리가 이미 딕셔너리에 있으면, 그 값을 1 증가
        else:
            category_count[category] = 1  # 만약 해당 카테고리가 딕셔너리에 없으면, 새로운 항목을 만들고 값을 1로 설정
    
    result = 1  # 곱셈에서 사용할 초기값
    
    for value in category_count.values():
        result *= (value + 1)  # 각 value에 1을 더한 후 result에 곱하여 result를 업데이트
                                # 각 의상을 안입는 경우의 수가 있기에 +1

    return result - 1  # 모두 안 입는 경우 제외
