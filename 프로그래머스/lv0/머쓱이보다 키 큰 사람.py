def solution(array, height):
    return sum(1 for person in array if person > height)