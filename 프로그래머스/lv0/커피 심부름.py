def solution(order):
    # 아메리카노 = 4500 / 카페 라테 = 5000
    # 메뉴를 적은 팀원 = 아이스 해당 메뉴 / 아무거나 = 차가운 아메리카노
    # order = 적은 메뉴 / 결제 금액 return
    answer = 0
    
    for i in order:
        if "americano" in i or i == "anything":
            answer += 4500
        else:
            answer += 5000
    return answer
        