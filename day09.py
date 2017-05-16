# Chapter 3 Structures that Control Flow
# while - 조건이 true일 동안 돌아간다

# for - Collection에 대한 Object의 개수만큼 돌아간다
# Collection의 범주 : List, String(Character 개수만큼), File Object
"""
for var in sequence:
var: sequence에 있는 각각의 object을 가리키는 변수
"""
months = {"January", "February"}
reversedWord = ""
for month in months:
    if 'r' in month.lower():
        reversedWord = ""
        for ch in month:
            reversedWord = ch + reversedWord
        print("The reversed word is " + reversedWord + ".")

# For 1. Arithmetic Progression : range(3, 10) - 3~9
# default는 1씩 건너 뛰는건데 이거에 대해서 조절을 하고 싶으면 파라미터를 하나 더 추가
# range (3, 10, 2) 이런식으로 !  이때 step = 2 겠지 물론 음수도 가능!
"""
for n in range(1, 9):
    for m in range(1, 10):
        print (m, 'x', n, '=', m*n, "\t", end="") # end="" 한이유는 ? 줄바꿈을 안하려고
    print()
"""
"""
# 이등변 삼각형 별 찍기
numberOfRows = int(input("Enter a number from 1 through 20: "))
for i in range(numberOfRows):
    for j in range(numberOfRows-1-i):
        print(" ", end="")
    for j in range(i*2+1):
        print ("*", end="")
    print()

# r 자가 들어가는 달의 이름을 모두 뒤집어서 찍어라
# ex / march 같은 경우엔 hcram
months = {"January", "February"}
reversedWord = ""
for month in months:
    if 'r' in month.lower():
        for ch in month:
            reversedWord = ch + reversedWord
        print("The reveersed word is " + reversedWord + ".")

# List는 안에 있는거를 바꿔치기 할 수 있다
months2 = ["January", "February"]
for i in range(len(months2)):
    months2[i] = months2[i][0:3]
print(months2)

# pass Statement - 그냥 돌리는게 목적
for i in 5:
    pass
"""