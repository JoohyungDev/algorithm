# https://100.pyalgo.co.kr/?page=11#

# def solution(data):
#     filtered_data = list(filter(lambda x:(x[0]+x[1]+x[2])/3>=80, data))
#     return len(filtered_data)

def solution(data):
    filtered_data = list(filter(lambda x:x[0]+x[1]+x[2]>240, data))
    return len(filtered_data)

# def solution(data):
#     return len([x for x in data if sum(x) > 240])