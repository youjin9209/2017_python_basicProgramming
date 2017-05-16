# Chapter 4. Functions
# example 4.1 4의배수+2의 문제 풀기 -> 5/13까지
"""
# Scope of Variable
# global variable: 누구나 읽고, 쓸수 있다 -> 권장하지 않아
# error example 1
def main():
    # 이 두줄이 만약 global로 되어있었으면 에러 안나지
    x = 5
    trivial()

def trivial():
    print(x) # x 는 global variable이 아니니까 ㅇㅋ

main()
"""

"""
# library modules - 동일한 코드의 반복을 function으로 만들어 놓고 이걸 reuse하겠다
# ex/ import finance.py
# __name__ == "__main__":
# ex/ A.py  B.py  C.py
# A.py안에 import b.py 있다, B.py안에는 import c.py가 있다
# B.py에서 run시키면 main은 B.py이다. 그때 __name__ == "__main__": 이 부분이 true가 되어 돌아간다
"""

"""
# Functions Returning Multiple Values
# 형식적으로는 single, 실질적으로는 multiple을 넘긴다
"""

"""
# List Comprehension - 어떤 리스트의 모든 element마다 function을 똑같이 적용하고 시퍼,
# 그 return value를 새로운 list로 저장
list2 = [f(x) for x in list1]
"""
"""
# Default Values
# default: 따로 얘기하지 않으면 그 값이야!/ 말하지 않으면 그냥 그값으로 알고 있는 암묵적인 value
ex/
def functionName(par1, par2, par3=10, par4=20):
# 주의 - 제일 끝부터 채워나가면서 / 제일 오른쪽 끝값부터 채워나가야함
# 이빨 빠지듯이 채우면 안됨
ex/ def total (w, x, y=10, z=20):

total(2, 3)
이면 w = 2, x =3이다
"""

"""
# Passing by Parameter Name: 변수의 이름을 주고 명시적으로 assignment할 수 있다.
# 순서 어길 수 있어
"""