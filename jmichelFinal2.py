#question 1 from final


print("select from menu")
print("_______________________")
print("Option 1")
print("Option 2")
print("Option 3")
print("_______________________")

option= int(input("Hello please enter a number to choose an option: "))

if (option == 1):
    name= input("Enter name: ")
    print(name, "Why did the yogurt go to the art exhibition?.......Because it was cultured!!")

elif (option ==2):
    food= input("What is your favorite food? ")
    for i in range(20):
        print(food)

elif (option ==3):
    value = 0
    guess = input

    while (guess != value):
        guess =float(input("enter the number zero: "))
        print("WARNING! WARNING! WARNING! You did not enter the number 0. Try Again.")

    if (guess == 0):
        print("Great, you entered 0! ")


