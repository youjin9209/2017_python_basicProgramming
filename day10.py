# Chapter 4 Functions
# example1
def isA(name): # return 타입이 다를 수 도 있다
    if (name[0] == 'a'):
        return True
    else:
        return "False"

def sub(a, b):
    return a-b

def listappend(names):
    names.append("ZZ")
def fToc(t):
    convertedTemp = (5/9)*(t-32)
    return convertedTemp

def triple (num):
    num = 3*num
    return num
"""
fahTemp = eval(input("Enter temp in fahren: "))
celsiusTemp = fToc(fahTemp)
print ("Celsius : ", celsiusTemp, "degrees")
num = 2
print (triple(num))
print (num)

a = 1
b = 2
mynames = ["apple", "banana"]
# immutable : int -> 변화가 안생겨
print (sub(a, b), sub(b, a)) # parameter의 order(position)에만 영향을 받는다
# mutable : list -> 변화가 생긴다
listappend(mynames)
print (mynames)
"""
name = "pple"
if isA(name):
    print ("YES") # 이게 찍힌다 string에 대해서는 empty가 아닌경우 true를 리턴하기 때문임
else:
    print("NO")

"""
def isA(name):
    if name[0] == 'a':
        return 1
    else:
        return "0"

name = "apple"
sum = isA(name) + 1
print (sum)

def isA(name):
    if name[0] == 'a':
        return 1
    else:
        return "0"

name = "pple"
sum = isA(name) + 1
print (sum)
"""

"""
# 존재를 알고 있어야 실행 가능 ㅇㅋ
#1
print (fun1(1, 2))
def fun1(a, b):
    return fun2(a, b)

def fun2(a, b):
    return a+b

-> func1 undefined error 남

#2
def fun1(a, b):
    return fun2(a, b)

print (fun1(1, 2))

def fun2(a, b):
    return a+b
-> func2 undefined error남

#3
def fun1(a, b):
    return fun2(a, b)

def fun2(a, b):
    return a+b

print (fun1(1, 2))
-> error안나
"""