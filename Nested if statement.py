num = int(input("Enetr the number :"))

if(num<0):
    print("number is negative")

elif(num>0):
    if(num<=10):
        print("number is between 1-10")

    elif(num>10 and num<=20):
        print("number is between 1-20")

    else:
        print("number is greater than 20")

else:
    print("numer is zero")

print("TASK IS COMPLETE")

