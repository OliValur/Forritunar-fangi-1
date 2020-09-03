import math

# m_str = input('Input m: ')  # do not change this line
# # change m_str to a float
# # remember you need c
# # e = 

# m_float = float(m_str)
# c = 300000000**2
# e = m_float*c
# print("e =", e)  # do not change this line)


# Einstein's famous equation states that the energy in an object at rest equals its mass times the square of the speed of light.  (The speed of light is 300,000,000 m/s.)

# Complete the skeleton code below so that it:
# * Accepts the mass of an object (remember to convert the input string to a number, in this case, a float).
# * Calculate the energy, e
# * Prints e

# import math

# x1_str = input("Input x1: ")  # do not change this line
# y1_str = input("Input y1: ")  # do not change this line
# x2_str = input("Input x2: ")  # do not change this line
# y2_str = input("Input y2: ")  # do not change this line

# x1_int = int(x1_str)
# y1_int = int(y1_str)
# x2_int = int(x2_str)
# y2_int = int(y2_str)
# formula =(y1_int-y2_int)**2+(x1_int-x2_int)**2
# d = math.sqrt(formula)
# print(formula)
# print("d =",d)  # do not change this line

# weight_str = input("Weight (kg): ") # do not change this line
# height_str = input("Height (cm): ") # do not change this line

# # weight_int = int(weight_str)
# # height_int = int(height_str)
# weight_float = float(weight_str)
# height_float = float(height_str)

# bmi = weight_float / (height_float**2)
# print("BMI is: ", bmi) # do not change this line75,290.6

n_str = input("Input n: ")
# remember to convert to an int
n_int = int(n_str)
first_three = n_int//100
last_two =n_int % 100

print("first_three:", first_three)
print("last_two:", last_two)

# Write a Python program that:

# Accepts a five-digit integer as input
# Assign the variable first_three (int) to be the first three digits.
# Assign the variable last_two (int) to be the last two digits.
# Prints out the two computed values.
# Hint: use quotient (//) and remainder (%)

# For example, if the input is 12345, the output should be:

# first_three: 123
# last_two: 45

# If the fourth digit is a zero, like 12305, the output should be:
# first_three: 123
# last_two: 5
# (even though that is not strictly correct).