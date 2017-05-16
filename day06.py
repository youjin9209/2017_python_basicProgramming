
"""
name = "abc"
print(name.upper())

words = ["spam", "ni"]
print (words.reverse())
print (words)
list1 = ['a',1]
list1.extend([2, 'b'])
#list1 = ['a', 1] + [2, 'b']

print (list1)
grades = []
num = float(input("Enter the first grade: "))
grades.append(num)
num = float(input("Enter the second grade: "))
grades.append(num)
num = float(input("Enter the third grade: "))
grades.append(num)
num = float(input("Enter the fourth grade: "))
grades.append(num)
num = float(input("Enter the fifth grade: "))
grades.append(num)

max_num = max(grades)
min_num = min(grades)
grades.remove(max_num)
grades.remove(min_num)

average = sum(grades)/len(grades)

print (average)


list1 = ['a', 'b', 'c']
print (list1[1:3])
print (list1)
del list1[1:3]
print (list1)

print("a,b,c".split(','))
print("you jin".split())

line = ["To", "be", "or", "not", "to", "be"]
print(" ".join(line))
krispies = ["Snap", "Crackle", "Pop"]
print(", ".join(krispies))

regions = [("Northeast", 55.3), ("Midwest", 66.9), ("South", 114.6), ("West", 1.9)]
print ("The 2010 population of the", regions[1][0], "was", regions[1][1], "million.")
totalPop = regions[0][1] + regions[1][1] + regions[2][1] + regions[3][1]
print ("Total 2010 population of the U.S: {0: .1f} millions.".format(totalPop))

# All because Lists are mutable
list1 = ['a', 'b']
list2 = list1
list2[1] = 'c'
print(list1)

# New note change
list3 = ['a', 'b']
list4 = list(list3) # list4 now points to different memory location
list4[1] = 'c'
#print(list3)
"""