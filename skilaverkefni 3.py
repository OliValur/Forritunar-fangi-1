# Fibonacci

# d1 = 0
# d2 = 1
# d3 = d1 + d2
# d1 = d2
# d2 = d3
# print(d3)
user_input = input("Input f|a|b (fibonacci, abundant or both: ")

fib1 = 0
fib2 = 1

if user_input == "f" or "b":
    fib_length = int(input("Input the length of the sequence: "))
    print(fib1)
    print(fib2)
    for num in range(fib_length-2):
        fib3 =  fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        print(fib3)

# if user_input == "a" or "b":
#     max_to_check_abundant = 30 #int(input("Input the max number to check: "))
#     for num in range(1,max_to_check_abundant+1):
#         number_sum = 0
#         for number in range(1,num):
#             if num % number == 0:
#                 number_sum += number
#             if number_sum > num:
#                 print(num)
#                 break

