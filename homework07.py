# Example 3.2, 3.3 8의 배수
#24
balance_end = 100
month = 1
while (balance_end <= 3000):
    balance_end = (1.0025)*(balance_end) + 100
    month = month + 1
print ("Annuity will be worth more than $3000 after %d months" %month)
"""
# 3.2
# 8
length = eval(input ("Enter length of cloth in yards: "))
if length < 1:
    cost = 3.00
else:
    cost = 3.00 + ((length-1)*2.50)
result = "Cost of cloth is ${0:0.2f}.".format(cost)
print (result)

#16
number = 6
if number > 5 and number < 9:
    print("Yes")
else:
    print("No")

#24
feet = eval(input("How tall (in feet) is the Statue of Liberty? "))
if (feet <= 141):
    print ("Nope")
if (feet > 141):
    if (feet < 161):
        print ("Good")
    else:
        print ("Nope")

# 32
consonant = 'ay'
vowel = 'way'
original = input('Enter word to translate: ')
word = original.lower()
first = word[0] + word[1]
if len(original) > 0 and original.isalpha() == True:
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        new_word_vowel = str(word) + str(vowel)
        print("The word in Pig Latin is "+new_word_vowel)
    else:
        new_word_consonant = str(word[2:]) + str(first) + str(consonant)
        print("The word in Pig Latin is "+new_word_consonant)

#40
length = eval(input ("Enter length of cloth in yards: "))
if length >= 1:
    cost = 3.00 + ((length-1)*2.50)
result = "Cost of cloth is ${0:0.2f}.".format(cost)
print (result)

# 3.3
#8
numTries = 0
year = 0
while(numTries < 7) and (year != 1964):
    numTries += 1
    year = int(input("Try #" + str(numTries) +": In what year " +
                     "did the Beatles invade the U.S.?"))
    if year == 1964:
        print ("\nYes. They performed on the Ed Sullivan show int 1964.")
        print ("You answerd correctly in " + str(numTries) + " tries.")
    elif year < 1964:
        print ("Later than", year)
    else: #year >1964
        print ("Earlier than", year)
if (numTries == 7) and (year != 1964):
    print ("\n Your 7 tries are up. The answer is 1964.")

#16
restitution = float(input ("Enter coefficient of restitution: "))
height = int(input("Enter initial height in meters: "))
bounces = 0
total = height
height_init = height
while(height >= 0.1):
    height = height*restitution
    total = total + height
    bounces = bounces + 1
total = total*2-height_init
print("Number of bounces: %d" %bounces)
print("Meters traveled: %f" %total)
"""