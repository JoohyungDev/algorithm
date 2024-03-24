# https://100.pyalgo.co.kr/?page=84#


def solution(data):
    sorted_data = sorted(data, key=lambda x: x.split(",")[2])
    return sorted_data[0].split(",")[0]


solution(["Flight D,08:00,10:00", "Flight E,08:30,10:30", "Flight F,07:45,10:15"])
