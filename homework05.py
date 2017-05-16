# Example 2.4 4의 배수
countries = ["Japan", "India", "Algeria", "Brazil", "Angola", "England", "Argentina",
             "Portugal", "China", "Australia", "Austria", "Ghana", "Bahamas",
             "Bangladesh", "Belgium", "Bhutan", "Bosnia", "Cameroon", "Canada",
             "Denmark"]

"""
countries = ["Japan", "India", "Algeria", "Brazil", "Angola", "England", "Argentina",
             "Portugal", "China", "Australia", "Austria", "Ghana", "Bahamas",
             "Bangladesh", "Belgium", "Bhutan", "Bosnia", "Cameroon", "Canada",
             "Denmark"]
#4.  8.  12.  16.  20.  24.  28.  32.  36.  40.
print (len(countries))
print (countries.index(countries[10]))
countries.insert(5, "Germany")
print (countries[5])
del countries[3]
print (countries.index("Argentina"))
print (countries[4:-1])
print (countries[:-1])
print (countries[-2:len(countries)])
print (len(countries[-20:]))
print (len(countries[2:-2]))
countries[1] = "Poland"
print (countries[:3])

# 44.  48
print ((','.join(countries[1:4])))
countries[-1].append("Spain")
print(countries[-1])

#52
print (countries[-8:-1])

#56
nums = [6, 2, 8, 0]
print ("Length: ", len(nums))

#60
L = ["one", "for", "all"]
L[0], L[-1] = L[-1], L[0]
print (L)

#64
list1 = ['h', 'o', 'n', 'P', 'y', 't']
list2 = list1[3:] + list1[:3]
print (list2)
print (("".join(list2)))

#68
carousel = ["merry", "go", "round"]
print (('-').join(carousel))

#72
nations = "France\nEngland\nSpain"
countries = nations.split()
print(countries)

#76
infile = open("/Users/scarlett/PycharmProjects/programming_python2017/Live.txt", 'r')
words = [line.rstrip() for line in infile]
words.append(words[0].lower())
quote = (" ").join(words) + '.'
print(quote)

# 80
word = "diary"
list1 = list(word)
list1.insert(3, list1[1])
del list1[1]
word = "".join(list1)
print(word)

# 84
t = (1, 2, 3)
t = (0, ) + t[1:]
print(t)

# 88
list1 = ["gold"]
list2 = ["silver", "bronze"]
list1.extend(list2)
print(list1)

#92
ships = ["Nina", "Pinta", "Santa Maria"]
print (ships[-5:2])

#96
word = "sea"
location = numbers.index(7)
word[1] = 'p'
print(word)

#100
words = ("Keep", "cool", "but", "don't")
words.append("freeze.")
print(words)

#104
full_name = input("Enter a 3-part name: " )
middle_name = full_name.split(" ")[1]
print (middle_name)
"""