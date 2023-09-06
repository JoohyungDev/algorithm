def solution(rsp):
    score = {'2':'0', '0':'5', '5':'2'}
    return ''.join([score[i] for i in rsp])
