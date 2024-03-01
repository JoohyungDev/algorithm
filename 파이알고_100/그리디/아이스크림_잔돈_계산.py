# https://100.pyalgo.co.kr/?page=52#


# def solution(data):
#     charge_dic = {"10000": 0, "5000": 0, "1000": 0, "500": 0, "100": 0}
#     charge = 10000 - 700 * data
#     for i in range(5):
#         if charge == 10000:
#             return [1, 0, 0, 0, 0]
#         else:
#             if charge >= 5000:
#                 charge_dic["5000"] += 1
#                 charge -= 5000
#             elif charge >= 1000:
#                 charge_dic["1000"], charge = divmod(charge, 1000)
#             elif charge >= 500:
#                 charge_dic["500"], charge = divmod(charge, 500)
#             elif charge >= 100:
#                 charge_dic["100"], charge = divmod(charge, 100)
#     return list(charge_dic.values())


def solution(data):
    charge_dic = {10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0}
    charge = 10000 - 700 * data
    if charge == 10000:
        return [1, 0, 0, 0, 0]
    else:
        for coin in [5000, 1000, 500, 100]:
            charge_dic[coin], charge = divmod(charge, coin)
    return list(charge_dic.values())


solution(2)
