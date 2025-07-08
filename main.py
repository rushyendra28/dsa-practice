# find area of a trainagle

# base = float(input("Enter the Base length of the traingle: "))
# height = float(input("Enter the height length of the traingle: "))

# area = 0.5 * base * height

# print(f"The area of the traingle is: {area}")


# swapping values of variables
# a = input("Enter the value of a: ")
# b = input("Enter the value of b: ")

# print(f"Original values of a and b are: {a} and {b}")

# temp = a
# a = b
# b = temp

# print(f"Swapped values of a and b are: {a} and {b}")


# Generate a random number between 1 and 1000
# import random
# print(f"Random number between 1 and 1000: {random.randint(1, 1000)}")



#km to miles conversion

# km = float(input("Entwe the distance in Kilometers: "))
# con_fac = 0.621371
# miles = km * con_fac
# print(f"The distance in miles is: {miles}")



#celcius to fahrenheit conversion

# c = float(input("Enter the temperature in celcius: "))
# f = c* 9/5 + 32
# print(f"The temperature in fahrenheit is: {f}")



#display calender

# import calendar

# year = int(input("Enter the year: "))
# month = int(input("Enter the month: "))
# cal = calendar.month(year, month)

# print(cal)



#solve quadratic equation

# import math

# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))

# discriminant = b**2 - 4*a*c

# if discriminant > 0:
#     root1 = (-b + math.sqrt(discriminant)) / (2*a)
#     root2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print(f"Root 1: {root1}")
#     print(f"Root 2: {root2}")

# elif discriminant == 0:
#     root = -b / (2*a)
#     print(f"Root: {root}")

# else:
#     realPart = -b / (2*a)
#     imaginaryPart = math.sqrt(-discriminant) / (2*a)
#     print(f"Root 1: {realPart} + {imaginaryPart}i")
#     print(f"Root 2: {realPart} - {imaginaryPart}i")


#swapping without temp

# a = 69
# b = 420
# print(f"Before swaping: {a} and {b}")
# a, b = b, a
# print(f"Swapped values of a and b are: {a} and {b}")


#check if the given number is positive, negative or zero
# num = int(input("Enter a number: "))

# if num > 0:
#     print(f"{num} is positive")
# elif num == 0:
#     print("Zero")
# else:
#     print(f"{num} is negative")


#check if numeber is even or odd
# num = int(input("Enter a number:"))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


#check for leap year
# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# check for prime number
# num = int(input("Enter a number: "))
# is_prime = True
# for i in range(2, int(num**0.5) + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num > 1:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")


#reverse string
str = input("Enter a string: ")
reversed_str = str[::-1]
print(f"Reversed string: {reversed_str}")