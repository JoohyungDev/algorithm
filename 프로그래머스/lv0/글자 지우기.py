def solution(my_string, indices):
    my_string = list(my_string)

    for i in range(len(my_string)):
        if i in indices:
            my_string[i] = " "
    cleaned_list = [item for item in my_string if item.strip() != ""]
    return "".join(cleaned_list)

# def solution(my_string, indices):
#     answer = ''
#     for i in range(len(my_string)):
#         if i not in indices:answer+=my_string[i]
#     return answer
