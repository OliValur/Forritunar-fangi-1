# print(int('4') != 4)

# x = 7
# y = (x < 7) or (x > 7)
# print(x,y)

# x = 10
# y = 12
# result = (x < y) and (y > 10) or (x < 10)
# print(result)

# a_int = 2
# b_int = 3
# b_int = a_int
# a_int = b_int
# print(a_int,b_int)

# --------------dæmi 1

# num = int(input("Input a number: ")) # Do not change this line

# if num < 0:
#     print("Negative")
# elif num == 0:
#     print("Zero")
# elif num > 0:
#     print("Positive")

# -------------- dæmi 2

# Write a program that prompts for chess elo rating (an integer).  A valid rating is > 999. 
#  A super grandmaster has rating >= 2700, a grandmaster rating >= 2500, and an international master has rating >= 2400. 
#    Let's call a chess player with rating < 2400 amateur.
#     Write a program that prints out  "Super grandmaster", "Grandmaster", "International", "Amateur", or "Invalid", 
#     depending on the input.

# rating = int(input("Input elo rating: ")) # Do not change this line
# # Fill in the missing code below
# if rating <= 999:
#     print("Invalid")
# elif rating >= 2700:
#     print("Super grandmaster")
# elif rating >= 2500:
#     print("Grandmaster")
# elif rating >= 2400:
#     print("International")
# else:
#     print("Amateur")

# -------------- dæmi 3
# num1 = int(input("First number: ")) # Do not change this line
# num2 = int(input("Second number: ")) # Do not change this line
# num3 = int(input("Third number: ")) # Do not change this line

# if num1 < num2 and num3:
#     min_int = num1
# elif num2 < num3 and num1:
#     min_int = num2
# else:
#     min_int = num3

# print("The minimum is: ", min_int) # Do not change this line


# ------------dæmi 4

# Accept d1 and d2, the number on two dice as input. First, check to see that they are in the proper range for dice (1-6). 
# If not, print the message "Invalid input". If d1 and d2 have the same value, print out "Pair".
#  Otherwise print the sum

# d1 = int(input("Input first dice: ")) # Do not change this line
# d2 = int(input("Input second dice: ")) # Do not change this line

# if d1<1 or d1>6 or d2<1 or d2>6:
#     print("Invalid input")
# elif d1 == d2:
#     print("Pair")
# else:
#     print(d1+d2)

# ----------- dæmi 5

# The theme park King’s Island needs to calculate its admission ticket prices. 
# When visitors come to the park and purchase tickets they might be eligible for a discount based on their age.
 
# Each ticket cost $40. Senior citizens (age >= 65) are given a 40% discount.  
# People under 20 years of age get a 20% discount, and children under, or equal to, the age of 5 get a free admission.
 
# Write a program that prompts for the visitor's age and computes and prints the ticket price (which should be a float).

# age = int(input("Input age: ")) # Do not change this line
# base_cost = 40

# if age >= 65:
#     final_cost = base_cost *0.6
# elif age <= 5:
#     final_cost = 0
# elif age < 20:
#     final_cost = base_cost *0.8
# else: 
#     final_cost = base_cost
# print(float(final_cost))

# ----------- dæmi 6

# Here is an algorithm to determine whether a year is a leap year:
 
#  1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
#  2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
#  3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
#  4. The year is a leap year (it has 366 days).
#  5. The year is not a leap year (it has 365 days).
 
# Write a program that prompts for a year and prints out True if the year is a leap year, otherwise False.

year = int(input("Input a year: ")) # Do not change this line

if year % 4 != 0:
    is_leap_year = False
elif year % 100 != 0:
    is_leap_year = True
elif year %400 != 0:
    is_leap_year = False
else:
    is_leap_year = True

print(is_leap_year)
