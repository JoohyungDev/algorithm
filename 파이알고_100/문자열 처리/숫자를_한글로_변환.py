# https://100.pyalgo.co.kr/?page=88#


def solution(data):
    my_dict = {
        0: "",
        1: "일",
        2: "이",
        3: "삼",
        4: "사",
        5: "오",
        6: "육",
        7: "칠",
        8: "팔",
        9: "구",
        10: "십",
        100: "백",
        1000: "천",
    }
    result = ""
    current_num = data
    if current_num // 1000 != 0:
        result += my_dict[data // 1000] + "천"
        current_num = data % 1000
    if current_num // 100 != 0:
        result += my_dict[current_num // 100] + "백"
        current_num = data % 100
    if current_num // 10 != 0:
        result += my_dict[current_num // 10] + "십"
        current_num = data % 10
    result += my_dict[current_num]
    return result


solution(9876)
