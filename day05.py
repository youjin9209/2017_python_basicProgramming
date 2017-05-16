print("0123456789012345678901234567")
print("{0: ^5s}{1: <20s}{2: >3s}".format("Rank", "Player", "HR"))
print("{0: ^5n}{1: <20s}{2: >3n}".format(1, "Barry Bonds", 762))
#print ("Hello", "World!", sep="*")
"""
#print("Rank".ljust(2))

print("0123456789012345678901234567")
print("{0:^5s}{1:<20s}{2:>3s}".format("Rank", "Player", "HR"))
print("{2:^5n}{1:<20s}{0:>3n}".format(1, "Barry Bonds", 762))
print("{0:^5n}{1:<20s}{2:>3n}".format(2, "Hank Aaron", 755))
print("{0:^5n}{1:<20s}{2:>3n}".format(3, "Babe Ruth", 714))

# 시험문제
print("The area of {0:s} is {1: ,d} square miles.".format("Texas", 268820))
str1 = "The Population of {0:s} is {1:.2%} of the U.S. population"
print(str1.format("Texas", 26448000/309000000))
"""