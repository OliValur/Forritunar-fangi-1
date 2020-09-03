# my_int = int(input("Enter a positive integer: "))

# while my_int > 0:
#     if my_int % 2 == 1:
#         my_int = my_int // 2
#     else:
#         my_int = my_int - 1

# print(my_int)

# print(5//2)

# number = int(input("Enter a positive integer: "))
# count = 0

# while number > 1:
#     if number % 2 == 0:
#         number = number // 2
#     elif number % 3 == 0:
#         number = number // 3
#     else:
#         number = number - 1
#     count = count + 1

# print(count)

# i = 1
# j = 1

# while i < 5:
#     i += 1
#     j += i
# print(i,j)

# num = int(input("Enter a number: "))

# while True:
#     if num % 3 == 0:
#         break
#     print(num)
#     num -= 1

# ------------- dæmi1 

# num = int(input("Input an int: ")) # Do not change this line

# while num > 0:
#     print(num)
#     num -= 1

#---------------- dæmi 2

# num = int(input("Input an int: ")) # Do not change this line
# multiplier = 1
# while num > 0:
#     print(2 * multiplier)
#     multiplier += 1
#     num -= 1

# # -------- dæmi 3

# num = int(input("Input an int: ")) # You can copy this line but not change it
# sum = 0
# while num != 10:
#     sum += num
#     num = int(input("Input an int: "))
# print(sum)

# -------- dæmi 4

# n = int(input("Input an int: ")) # Do not change this line
# i = 1

# while i <= n:
#     if n % i == 0:
#         print(i)
#     i +=1

# -------- dæmi 5

# rating = int(input("Input elo rating: ")) # Do not change this line

# while rating > 0:
#     if rating < 1000:
#         print("Invalid")
#     elif rating >= 2700:
#         print("Super grandmaster")
#     elif rating >= 2500:
#         print("Grandmaster")
#     elif rating >= 2400:
#         print("International")
#     else:
#         print("Amateur")
#     rating = int(input("Input elo rating: "))

# ----------- dæmi 6

# a0 = int(input("Input a positive int: "))   # Do not change this line
# print(int(a0))
# while a0 != 1:
#     if a0 % 2 == 0:
#         a0 /= 2
#     else:
#         a0 = 3 * a0 + 1
#     print(int(a0))

num = int(input("Enter a number: "))

while True:
    if num % 3 == 0:
        break
    print(num)
    num -= 1