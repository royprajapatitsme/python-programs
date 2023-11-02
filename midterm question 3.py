input_list = input("Enter a list of integer separated by space :").split()

input_list = [int(x) for x in list]

result_list = [x**2 for x in input_list if (x**2)%2 != 0]

if result_list:
    print(*result_list)

else:
    print("none")
