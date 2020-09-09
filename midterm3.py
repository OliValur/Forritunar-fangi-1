import math

start_int = int(input("Input starting integer: "))
current_int = start_int

while current_int >= 2:
    current_int = math.sqrt(current_int)
    print(round(current_int,4))