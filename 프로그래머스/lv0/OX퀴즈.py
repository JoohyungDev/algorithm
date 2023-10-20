def solution(quiz):
    result = []
    
    for i in quiz:
        left_side, right_side = i.split("=")

        # 앞뒤 공백 제거
        left_side = left_side.strip()
        right_side = right_side.strip()

        # 각 부분 계산
        left_result = eval(left_side)
        right_result = eval(right_side)

        if left_result == right_result:
            result.append("O")
        else:
            result.append("X")
            
    return result
