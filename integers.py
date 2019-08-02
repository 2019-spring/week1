# numbers >> integers, floats

# number1 = input("Enter your first number: ")
# number2 = input("Enter your second number: ")
# converting the old values of variables from string to integers
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

# operations with numbers
sum = number1 + number2
multiplication = number1 * number2
division = number1 / number2
# modulo
remainder = number2 % number1
remainder1 = number1 % number2

division_floor = number2 // number1  # 30//25
division_floor1 = number1 // number2  # 25//30


# print(sum)
# print(multiplication)
# print(division)
# print(remainder)
# print(remainder1)
# print(division_floor)
# print(division_floor1)

# using numbers with strings : using str() - converts numbers to strings, int() - converts strings to integers
# print("Sum of number1 and number2 is : " + str(sum))
print("Sum of " + str(number1)+" and " + str(number2) + " is : " + str(sum))
print("Multiplication of number1 and number2 is : " + str(multiplication))
print(division)
print(remainder)
print(remainder1)
print(division_floor)
print(division_floor1)

# fstring 
print("**** using fstring ****************** ")
print(f"Sum of {number1} and {number2} is : {sum}")
print(f" {number1} minus {number2} is : {number1 - number2}")

age = "25" # this is the string not integer
print(age)
age = int(age) + 12 #      age += 12
print(age)
# age++ >> age = age + 1
# age-- >> age = age - 1