# Example 4.2 (8의 배수)
#70
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def isPrime(num):
    if (factorial(num-1)+1)%num == 0:
        return True
    else:
        return False

num = int(input("Enter an integer greater than 1: "))

if isPrime(num) == True:
    print(num, end="")
    print(" is a prime number.")

"""
#8
list1 = ["pear", "Banana", "apple"]
list1.sort(reverse=True)
print(list1)
list1.sort(key=lambda x:len(x), reverse=True)
print(list1)

#16
def main():
    list1 = ["e", "pluribus", "unum"]
    list2 = sorted(list1, key=numberOfVowels)
    print(list2)

def numberOfVowels(word):
    return len([ch for ch in word if (ch in "aeiou")])

main()

#24
popLanguages = ["Python", "Java", "C", "C++", "Ruby", "VB", "PHP"]
sentence = "I program in VB, Python, and Ruby."
list1 = sentence.split()
myLanguage = [word[:-1] for word in list1 if word[:-1] in popLanguages]
for language in myLanguage:
    print (language, end = "  ")

#32
numbers = [9, -5, 4, 1, -7]
new_numbers = []
for num in numbers:
    if num >= 0:
        new_numbers.append(num)
newList = [x ** .5 for x in new_numbers]

print(newList)

#40
def bestFilm(year, film, star):
    print(year)
    print(film)
    print(star)

bestFilm(star="Ben Affleck", film="Argo", year=2012)

#48.
print("".join(sorted("pengos", reverse=True)))

#56.
Planets = [("Mercury", 75, 1), ("Venus", 460, 2), ("Mars", 140, 4), ("Earth", 510, 3),
           ("Jupiter", 62000, 5), ("Neptune", 7640, 8), ("Saturn", 42700, 6),
           ("Uranus", 8100, 7)]
Planets.sort(key=lambda x:len(x[0]))
print("Sorted by length of name of planet in ascending order: ")
for item in Planets:
    print(item[0] + "  ", end="")
"""