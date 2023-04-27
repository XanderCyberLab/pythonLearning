####### Conditions If/Else Statements ########
# if condition:
#     do this
# else:
#     do this
   
#Modulo: Even or Odd
print("Check if your number is Even or Odd")
number = float(input("Please enter a number "))

if number % 2 == 0:
    print("Your number is Even")
else:
    print("Your number is Odd")

####### Nested Conditions If/Else Statements ########
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

print("Are you tall enough for the rollercoaster?")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("Please enter your age "))
    if age < 12:
        print("You pay $5")
    elif age < 18:
        print("You pay $7")
    else:
        print("You pay $12")    
else:
    print("Sorry, you're too short")