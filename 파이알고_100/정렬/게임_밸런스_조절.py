# https://100.pyalgo.co.kr/?page=10#

def solution(data):
    filtered_data = list(filter(lambda x:(x[1]+x[2]+x[3]+x[4])>=350, \
                                data))
    sorted_data = sorted(filtered_data)
    return [i[0] for i in sorted_data]