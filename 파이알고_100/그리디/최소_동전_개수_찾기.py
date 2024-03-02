# https://100.pyalgo.co.kr/?page=51#


# def solution(data):
#     coins, amount, count = data["coins"], data["amount"], 0
#     coins = sorted(coins, reverse=True)
#     for i in range(100):
#         if amount == 0:
#             return count
#         while coins[i] <= amount:
#             amount -= coins[i]
#             count += 1
#     return -1


def solution(data):
    coins, amount, count = data["coins"], data["amount"], 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        if coin <= amount:
            num, amount = divmod(amount, coin)  # 몫과 나머지
            count += num
        if amount == 0:
            return count
    return -1  # 주어진 동전들로 amount를 만들 수 없는 경우


solution({"coins": [1, 5, 10], "amount": 18})
