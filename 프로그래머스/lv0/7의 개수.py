def solution(array):
    return sum(str(i).count("7") for i in array if "7" in str(i))

# def solution(array):
#     return str(array).count('7')