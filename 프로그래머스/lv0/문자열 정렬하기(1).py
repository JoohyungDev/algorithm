def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    sorted_list = sorted(answer)
    return sorted_list

# def solution(my_string):
#     return sorted([int(c) for c in my_string if c.isdigit()])
