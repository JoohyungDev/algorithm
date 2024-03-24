# https://100.pyalgo.co.kr/?page=85#


def solution(data):
    airports, patientData = data

    n_dict = {i["name"]: (i["distance"], i["treatableDiseases"]) for i in airports}
    air_list = list()

    n_d = sorted(n_dict.items(), key=lambda x: x[1][0])

    for i in n_d:
        if i[1][1] == patientData:
            return [i[0]]

    for i in n_d:
        for treat in i[1][1]:
            if treat in patientData:
                patientData.remove(treat)
                air_list.append(i[0])

    return air_list


solution(
    [
        [
            {
                "name": "Airport A",
                "distance": 500,
                "treatableDiseases": ["Disease A", "Disease B"],
            },
            {"name": "Airport B", "distance": 300, "treatableDiseases": ["Disease C"]},
            {
                "name": "Airport C",
                "distance": 400,
                "treatableDiseases": ["Disease B", "Disease C"],
            },
        ],
        ["Disease A", "Disease C"],
    ]
)
