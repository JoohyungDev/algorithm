# https://100.pyalgo.co.kr/?page=83#


def solution(data):
    result = []
    sorted_data = sorted(data, key=lambda x: x["start"])
    pre_start = sorted_data[0]["start"]
    pre_end = sorted_data[0]["end"]
    pre_credit = sorted_data[0]["credit"]
    for i in sorted_data:
        if len(result) == 0:
            result.append(i)
        else:
            if pre_start <= i["start"] < pre_end:
                if i["credit"] > pre_credit:
                    result.pop()
                    result.append(i)
                    continue
                else:
                    continue
            if i["start"] != pre_start and i["end"] != pre_end:
                result.append(i)
                pre_start, pre_end = i["start"], i["end"]
    return [i["name"] for i in result]


solution(
    [
        {
            "name": "알고리즘",
            "type": "전공 필수",
            "start": "09:00",
            "end": "10:30",
            "instructor": "이교수",
            "credit": 3,
        },
        {
            "name": "데이터베이스",
            "type": "전공 필수",
            "start": "10:30",
            "end": "12:00",
            "instructor": "한교수",
            "credit": 4,
        },
        {
            "name": "인공지능",
            "type": "전공 선택",
            "start": "10:45",
            "end": "12:15",
            "instructor": "박교수",
            "credit": 3,
        },
    ]
)
