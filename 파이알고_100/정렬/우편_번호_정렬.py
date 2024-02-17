# https://100.pyalgo.co.kr/?page=12#

def solution(data):
    address = data[0]
    post = data[1]
    
    sorted_data = sorted(address, key=lambda x:\
                         post[x.split()[1]]) 
    return sorted_data