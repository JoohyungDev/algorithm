def solution(myString, pat):
    my_string = myString.lower()
    my_pat = pat.lower()

    return 1 if my_pat in my_string else 0
