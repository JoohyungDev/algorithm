# https://100.pyalgo.co.kr/?page=15#

def solution(data):
    from datetime import datetime
    # (24시간제 시간, 12시간제 시간)
    converted_times = [(datetime.strptime(time, '%I:%M %p').strftime('%H:%M'), time) for time in data]
    sorted_times = sorted(converted_times)
    result = [time[1] for time in sorted_times]
    return result

# strftime = string format time을 뜻하며 datetime객체를 문자열로 바꿔준다.
# strptime = string parse time을 뜻하며 문자열을 datetime 형식으로 바꿔준다.
# 형식 지정자에는 다음이 있다. 
# %Y(네 자리 연도), %m(두자리 월), %d(두자리 일), %H(24시간 형식 두자리 시간)
# %I(12시간 형식 두자리 시간), %M(두 자리 분), %S(두 자리 초), %p(AM/PM 지시자)