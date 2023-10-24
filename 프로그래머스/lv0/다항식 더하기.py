def solution(polynomial):
    # 공백 제거 후 "+" 기호로 나눠서 항목들을 얻음
    polynomial = polynomial.split(" + ")

    # 각 x의 계수와 상수들의 합계 초기화
    sum_x = 0
    sum_const = 0

    for term in polynomial:
        if 'x' in term:   # 일차 항 처리
            coef = term.replace('x', '')
            coef = int(coef) if coef != "" else 1   # 계수가 생략된 경우 1로 처리
            sum_x += coef
        else:             # 상수 처리
            sum_const += int(term)

    result_terms = []
    
    if sum_x > 1:
        result_terms.append(f"{sum_x}x")
    elif sum_x == 1:
        result_terms.append("x")
    
    if sum_const > 0:
        result_terms.append(str(sum_const))

    return " + ".join(result_terms)
