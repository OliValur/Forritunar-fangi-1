max_int = int(input("Input max integer: "))
current_str = ""

for num in range(1,max_int+1):
    num_str = str(num)
    current_str += num_str + " "
    print(current_str)

