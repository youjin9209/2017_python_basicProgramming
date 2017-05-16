# Example 4.1 (8의 배수+2)
#34
def main():
    age = getAge()
    monthsOfService = getMonthsOfService()
    salary1 = getFirstSalary()
    salary2 = getSecondSalary()
    salary3 = getThirdSalary()
    pension = calculatePension(age, monthsOfService, salary1, salary2, salary3)
    displayPension(pension)

def getAge():
    age = (int)(input("Enter your age: "))
    return age

def getMonthsOfService():
    monthsOfService = int(input("Enter number of months of service: "))
    return monthsOfService

def getFirstSalary():
    salary1 = float(input("Enter first of three highest salaries: "))
    return salary1

def getSecondSalary():
    salary2 = float(input("Enter second of three highest salaries: "))
    return salary2

def getThirdSalary():
    salary3 = float(input("Enter third of three highest salaries: "))
    return salary3

def calculatePension(age, monthsOfService, salary1, salary2, salary3):
    ave = round((salary1 + salary2 + salary3) / 3, 2)
    yrs = monthsOfService / 12
    percentage = 1.5 * 5 + 1.75 * 5 + (2 * (yrs - 10))
    if percentage > 80:
        percentage = 80
    pension = ave * float(percentage / 100)
    return pension

def displayPension(pension):
    print("Annual pension: ", pension)

main()
"""
#10
def main():
    commonFates()
    print("died")
    commonFates()
    print("survived")

def commonFates():
    print("divorced")
    print("beheaded")

main()

#18
ESTATE_TAX_EXEMPTION = 1000000
TAX_RATE = .45
def main():
    valueOfEstate = 3000000
    tax = TAX_RATE*(valueOfEstate-ESTATE_TAX_EXEMPTION)
    print("You owe ${0: ,.2f} in estate taxes.".format(tax))

main()

#26
def function(string, str_to_search_for):
    count = 0
    for x in range(len(string) - len(str_to_search_for) + 1):
        if string[x:x + len(str_to_search_for)] == str_to_search_for:
            count += 1
    return count


print (function('1011101111', '11'))
"""