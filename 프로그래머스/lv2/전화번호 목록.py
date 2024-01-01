def solution(phone_book):
    answer = True
    phone_book.sort()

    for idx, i in enumerate(phone_book):
        if idx+1 < len(phone_book):
            if phone_book[idx+1][0:len(i)] == i:
                return False

    return answer

# def solution(phone_book):
#     answer = True
#     hash_map = {}

#     for phone_number in phone_book:
#         hash_map[phone_number] = 1 

#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 return False

#     return answer
