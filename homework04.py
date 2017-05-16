# Example 2.3 4의 배수

"""
# 4, 8, 12, 16, 20
print("Py", "th", "on", sep="")
print("one", " two", " three", sep=",")
print ("on", "site" ,sep='-', end="")
print ("repair")
print("1\t2\t3")
print("\tDetroit\tLions")
print("Indiana\t\tColts")
print ("STATE\tCAPITAL".expandtabs(15))
print("North Dakota\tBismarck".expandtabs(15))
print("South Dakota\tPierre".expandtabs(15))

# 24, 28, 32
print("01234567890")
print("{0:5s}{1:^5s}{2:5s}".format("A", "B", "C"))
print("{0:,.0f}".format(1234.567))
print("{0:14s}{1:s}".format("Major", "Percent of Students"))
print("{0:14s}{1:10.1%}".format("Biology", .062))
print("{0:14s}{1:10.1%}".format("Psychology", .054))
print("{0:14s}{1:10.1%}".format("Nursing", .047))

# 36, 40
print("And now for {0:s} completely {1:s}.".format("Something", "different"))
pi = 3.14159265898
print ("Pi is approximately {0:.3f}".format(pi))

#44, 48
str1 = "{0:.0%} of the members of the U.S. Senate are from {1:s}."
print(str1.format(12 / 100, "New England"))
print ("When you have {0:s} to {1:s}, {1:s} {0:s}.".format("nothing", "say"))

#52
print("Hello\tWorld!") # default tab = 8
print ("Hello\tWorld!".expandtabs(8))

#56
beginning_salary = int(input("Enter beginning salary: "))
new_salary = ((beginning_salary*1.05)*1.05)*1.05
change = (new_salary-beginning_salary)/new_salary*100
print ("new_salary: $%f" %new_salary)
print ("Change: %f" %change)
"""