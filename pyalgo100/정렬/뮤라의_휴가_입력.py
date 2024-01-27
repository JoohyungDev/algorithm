# https://100.pyalgo.co.kr/?page=16#

def solution(data):
    from datetime import datetime
    result = []

    for i in data:
        if '-' in i:
            date_format = '%d-%m-%Y'
        elif '/' in i:
            date_format = '%m/%d/%Y'
        else:
            date_format = '%Y.%m.%d'
        
        date = datetime.strptime(i, date_format)
        result.append(date)
    
    result.sort()

    return [i.strftime('%Y/%m/%d') for i in result]