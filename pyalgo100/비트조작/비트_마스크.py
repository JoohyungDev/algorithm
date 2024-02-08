import functools, operator

def solution(data):
    # functools.reduce()는 시퀀스형 자료형의 모든 요소에 주어진 함수를 적용한 결과 반환
    # functools.reduce(함수, 시퀀스자료형)
    # operator 모듈은 특정 연산자의 결과를 반환한다.
    and_ = functools.reduce(operator.and_, data)
    or_ = functools.reduce(operator.or_, data)
    return (and_, or_)

print(solution([7, 14, 3]))