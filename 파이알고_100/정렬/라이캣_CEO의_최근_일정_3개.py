# https://100.pyalgo.co.kr/?page=17#

def solution(data):
    from datetime import datetime
    # 모든 일정을 담을 리스트
    all_schedules = []

    for day, dates in data.items():
        for date in dates:
            # 일정의 날짜를 datetime 객체로 변환
            date_object = datetime.strptime(date, '%Y-%m-%d')
            # 일정의 날짜와 요일을 튜플로 묶어서 리스트에 추가
            all_schedules.append((date_object, day))

    # 일정을 날짜에 따라 내림차순으로 정렬
    all_schedules.sort(reverse=True)

    # 최근 3개의 일정을 선택
    recent_schedules = all_schedules[:3]

    # 선택된 일정을 'YY-MM-DD 요일' 형식의 문자열로 변환
    recent_schedules_str = [datetime.strftime(date, '%y-%m-%d') + ' ' + day for date, day in recent_schedules]
    return recent_schedules_str