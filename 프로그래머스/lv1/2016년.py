def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']     # 요일
    month = {"1":31, "2":29, "3":31, "4":30, "5":31, "6":30, "7":31, "8":31, "9":30, "10":31, "11":30, "12":31}     # 월과 일수 딕셔너리
    
    total_days = 0  # a월까지 총 일수 
    
    for key in month:
        if int(key) < a:
            total_days += month[key]
        else:
            break
    
    total_days += b
            
    return day[(total_days%7)-1]