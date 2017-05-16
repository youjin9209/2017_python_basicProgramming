# 1
"""
list = [7, 3, 2, 1, 10]
min = max(list)

for i in range(len(list)):
    if min > list[i]:
        min = list[i]
print (min)
"""
#2
list = [7, 3, 2, 1, 10]
max = min(list)
for i in range(len(list)):
    if max < list[i]:
        max = list[i]
print(max)

"""
months = ["January", "February", "March", "April", "May",
          "June", "July", "August", "September", "October",
          "November", "December"]
reversedWord = ""
for i in range(len(months)):
    months[i] = months[i][0:3]

for month in months:
    if 'r' in month:
        reversedWord = ""
        for ch in month:
            reversedWord = ch + reversedWord
        print("The reversed word is " + reversedWord + ".")
"""