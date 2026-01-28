#jessica michel lab 8 final project

name= input("Enter name: ")

print("select from menu")
print("_______________________")
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("Option 6")
print("_______________________")

option= int(input("Hello please enter a number to choose an option: "))

if (option == 1):
	print("Why did the computer go to the doctors? ..... Because he thought he had a terminal illness")

if (option == 2):
	for i in range(15):
		print(name)

elif (option == 3):
	num = int(input("enter a number: "))
	for i in range(num):
		print("You miss 100 percent of the shots you never take.") 

elif (option ==4):
	x=float(input("guess what number i am thinking about between 1-100:"))
	guess = 7

	while (x < 0):
		print("You did not enter a positive value")
	if (x< guess):
		print("You have entered ",x," and your guess is too small,try again")
	elif (x > guess):
		print("You have entered ",x," and your guess is too large, try again.")
	elif (x == guess):
		print("You have guessed ",x," and you are right! YAY, YOU WIN!")

#option 5 is conversion of F to C
elif (option ==5):
	x=float(input("Enter the temperature in Fahrenheit:"))	
	celsius= ((x-32)*(5/9))
	print(x,"degrees F is equal to",celsius,"degrees C") 
	

#option 6 is a silly sentence generator

elif (option  ==6):
	print("Welcome to your silly story!!")
	print("First, you will need to answer a few questions to help me fill in the blanks!")

#collecting user input
	name2= input("What should I call you? ")
	age= input("How old are you? ") 
	color= input("What is your favorite color? ")
	sport= input("What is your favorite sport? ")
#story time
	print("Hello everyone, I have some breaking news about",name2,"!" ,name2,  "is a",age,"year old that has been causing havoc in the entire city! Please beware of this individual. They were spotted wearing a ",color, "cape and a hat that has confetti bursting out of it every 5 seconds. Sometimes they can be found playing" ,sport,"at the zoo with some of the animals in their habitats! Absolute madness!")

 

