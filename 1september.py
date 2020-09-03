# upto = int(input("Input an int: "))  # Do not change this line

# for num in range(0,upto):
#     print(num)


# highest = int(input("Input an int: "))

# for num in range(1,highest+1):
#     if num % 3 == 0:
#         print(num)


# max_days = int(input("Input max number of days: "))
# target = int(input("Input dollar target: "))
# dollars = 1
# days_when_amount_acquired = 0

# for num in range(1,max_days+1):
#     dollars *= 2
#     if dollars >= target:
#         days_when_amount_acquired = num
#         break
# print('Days needed:',days_when_amount_acquired)

# Write a Python program using nested for loops that, given an integer n as input, prints all consecutive sums from 1 to n.

# For example, if 5 is entered, the program will print five sums of consecutive numbers:

# 1
# 3
# 6
# 10
# 15
# because

# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# length = int(input("Input the length of series: "))
# sum = 0
# final_sum = 0
# for i in range(length):
#     sum += 2
#     if i % 2 == 0:
#         print(sum)
#         final_sum += sum
#     else:
#         print(sum*(-1))
#         final_sum -= sum
# print(final_sum)

max_days = 4
target = 16
dollars = 1
days_when_amount_acquired = 0

for num in range(1,max_days+1):
    dollars *= 2
    if dollars >= target:
        days_when_amount_acquired = num
        break


print('Days needed:',days_when_amount_acquired)