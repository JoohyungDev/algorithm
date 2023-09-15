def solution(str_list):
    if "l" not in str_list and "r" not in str_list:
        return []
    elif "l" not in str_list:
        return str_list[str_list.index("r")+1:]
    elif "r" not in str_list:
        return str_list[:str_list.index("l")]
    else:
        if str_list.index("l") < str_list.index("r"):
            return str_list[:str_list.index("l")]
        if str_list.index("r") < str_list.index("l"):
            return str_list[str_list.index("r")+1:]
    
# def solution(str_list):
#     for i in range(len(str_list)):
#         if str_list[i]=='l': return str_list[:i]
#         elif str_list[i]=='r': return str_list[i+1:]
#     return []