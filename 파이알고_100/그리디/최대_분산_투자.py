# https://100.pyalgo.co.kr/?page=53#


def solution(data):
    opportunity, target = data
    opportunity = sorted(opportunity)
    result = []
    for cost, company in opportunity:
        if cost > target:
            continue
        result.append(company)
        target -= cost
        if target == 0:
            break
    return result


solution(([(200000, "A기업"), (300000, "B기업"), (400000, "C기업")], 500000))
