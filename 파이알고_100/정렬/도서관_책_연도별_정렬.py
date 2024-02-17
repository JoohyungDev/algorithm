# https://100.pyalgo.co.kr/?page=13#

def solution(data):
    books = data[0]
    pub_year = data[1]
    sorted_data = sorted(books, key=lambda x: (pub_year[x], x))
    return sorted_data