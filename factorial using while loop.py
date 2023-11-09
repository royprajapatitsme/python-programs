num = int(input("enter a positive integer number: "))
f = 1
while num:
    f = f*num
    num = num-1
    print("factorial of ", num, " is ", f)
