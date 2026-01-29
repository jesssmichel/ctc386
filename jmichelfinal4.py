def user_value():
 

    x= int(input("Enter an number between 1-10: "))

    if (x > 10):
        print("The number entered is too large.")
    else:
        for i in range(x):
            print("Happy New Year!!")

#calling on the function
user_value()

