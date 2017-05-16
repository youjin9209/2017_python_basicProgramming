# Chapter 3 Structures that Control Flow

"""
# ascii 를 기준으로 대소비교를 한다
# 우선순위: Numeric (+, - ) > Logical(and, or)
# Logical Operator
n = 4
ans = "Y"
print (2<n and n<6)
print ((2<n) or (n==6))
print (not(n<6))
print ((ans == "Y") or (ans=="y"))
print ((ans== "Y") and (ans=="Y"))
print (not(ans == "Y"))
print (((2 < n) and (n == 5+1)) or (ans =="No"))
print (((n==2) and (n==7)) or (ans == "Y"))

# 연산순위 : and > or. and 가 먼저다
print ((n==2) and (n==7) or (ans == "Y"))
print ((ans == "Y") or (n==7) and (n==2))

# Short Cut Evaluation
# (number != 0) and (m == n (n/number)) -> number != 0에서 걸려버리면 두번째 조건을 아예 시도도 안해버림

# bool data type
x = 2
y = 3
var = x < y  # bool type
print (var) # true

# methods that Return Boolean Type
str1 = "youjin Hello"
str2 = "youjin Hello hahaha"
str1.startswith(str2)
str1.endswith(str2)

print (isinstance(str1, str))
"""

# if - else Statements
# if - 조건을 만족하면 -> 다음 수행문을 실행하고
# else - 조건을 만족하지 않으면, -> else 부분을 수행하고
# if, else 를 벗어난 다음줄 -> if, else 를 끝내고 나서 수행해라
# python 에서는 indentation은 문법적 요소이다
"""
n = 10
if (n == 10):
    print ("hi youjin")
else:
    print ("hi hahaha")

# else가 없을 때
n = 10
if (n == 10):
    print ("hi youjin")
print ("hi hahaha")

# input을 통해 받는 타입은 기본적으로 string이라고 생각함. 그래서 eval을 통해 숫자로 바꿔줌
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))

if (num1 > num2):
    largerValue = num1
else:
    largerValue = num2
print ("The Larger value is", str(largerValue) + ".")
"""