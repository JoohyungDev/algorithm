def solution(price, money, count):
    # 이용료 = price, 현재 금액 = money, count = 몇번 탔는가
    # 부족한 금액을 return
    cost = 0    # 각 횟수당 이용 금액
    total = 0   # 이용 금액 합계
    
    for i in range(1,count+1):
        cost = price * i
        total += cost
    
    if total <= money:
        return 0
    else:
        return total-money
        