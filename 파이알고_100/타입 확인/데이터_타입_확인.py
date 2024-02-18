# https://100.pyalgo.co.kr/?page=19#

def solution(data):
    type_names = []

    for data in data:
        data_type = type(data).__name__
        type_names.append(data_type)
    return type_names

# type에는 다양한 메서드 들이 있다.
# type함수의 name매직 메서드를 출력하면 해당 데이터의 타입 이름이 나온다!
# __name__ 메서드는 if __name__ == "__main__"이런 형태로도 쓰이는데
# test1.py라는 파일이 있다고 하자
# print(__name__)이라고 하면 __main__이 출력된다.
# 만약에 test2.py라는 파일에서 test1.py를 import 한다고 가정

# test1.py의 내용
print("안녕")
# test2.py의 내용
import test1
print("hello")

# 위와 같은 상황에서 test2.py를 실행하면 test1의 안녕 + test2의 hello
# 2개가 동시에 출력된다.
# 따라서 모듈의 내용을 내가 원할때만 사용하려면
# if __name__ == "__main__":
#    print("hello")
# 위와 같이 사용한다. 