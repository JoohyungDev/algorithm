# https://100.pyalgo.co.kr/?page=63#


def solution(data):
    text, N = data
    result = []
    # "hello"라는 문자열에서 2-gram을 추출한다고 할 때, 시작 위치는 'h', 'e', 'l', 'l'까지 가능하고,
    # 'o'에서 시작하는 2-gram은 불가능
    for i in range(len(text) - N + 1):
        # 한칸씩 옆으로 이동
        result.append(text[i : i + N])
    return result


solution(["hello", 2])
