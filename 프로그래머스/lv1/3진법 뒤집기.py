def solution(n):
    # n을 3진법으로 만들고 뒤집는다
    # 이를 10진법으로 표현한다
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    return int(rev_base,3)