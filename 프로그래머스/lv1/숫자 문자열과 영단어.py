def solution(s):
    num_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7',
              'eight':'8', 'nine':'9'}
    answer = '' # 최종 문자열
    my_str = '' # 딕셔너리와 s의 문자 매칭용
    
    for i in s:
        if i in num_dic.values():
            answer += i
        else:
            my_str += i
        if my_str in num_dic.keys():
            answer += num_dic.get(my_str)
            my_str = ''
    
    return int(answer)
        