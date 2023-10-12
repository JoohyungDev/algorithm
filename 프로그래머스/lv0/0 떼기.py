def solution(n_str):
    for i,str in enumerate(n_str):
        if str != "0":
            return n_str[i:]
        