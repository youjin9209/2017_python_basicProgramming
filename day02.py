"""
#abs, int, round function
a = 2
b = 3
print (abs(1-(4*b)))
print (int((a**b) + .8))
print (round(float(a/b), 3))
"""

#Augmented Assignment
var = 1
var = var + 1
var += 1
print ("var: %d" %var)

#Augmented Assignment - Example4
num1 = 6
num1 += 1
num2 = 7
num2 -= 5
num3 = 8
num3 /= 2
print(num1, num2, round(num3))

num1 = 1
num1 *= 3
num2 = 2
num2 **= 3
print (num1, num2)

#integer division operator, modulus operator
totalInches = 41
feet = totalInches // 12
inches = totalInches % 12
print (feet, inches)

#runtime error
#print (5/0)