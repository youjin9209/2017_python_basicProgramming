# Chapter 3 Structures that Control Flow

"""
num1 = eval(input ("Enter the first number : "))
num2 = eval(input ("Enter the second number : "))

if num1 > num2:
    print ("The larger value is ", str(num1) + ".")
elif num2 > num1:
    print ("The larger value is ", str(num2) + ".")
else:
    print ("The two values are equal.")


# if / elif 순서가 중요하다
# if / if   순서 필요없고 조건 만족하면 다 얻어 걸린다.

# while - 제일 처음에 condition (bool type) check

num = 1
while num <= 5:
    print (num)
    num += 1

# Example 3: Find min, max, average
count = 0
total = 0
#num = eval(input("Enter number: ")) -> 이줄을 없애고 똑같은 효과가 날수 있게
num = 0
min = 100000 # 굉장히 큰 수를 넣는다  - 무조건 바뀌게
max = -1    # 굉장히 작은 수를 넣는다 - 무조건 바뀌게
while num != -1:
    count += 1
    total += num
    if num < min:
        min = num
    if num > max:
        max = num
    num = eval(input("Enter number: "))

# continue - while문을 계속 돌되, 20줄 중에서 10줄만 수행하고 밑의 10줄은 수행하고 싶지 않을 때
"""