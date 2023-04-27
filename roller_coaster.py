print("Welcome to the Roller Coaster")
height = float(input("How tall are you?"))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Please enter your age "))    
    if age < 12:
        bill = 5
        print("Kids Tickets are $5")
    elif age < 18:
        bill = 9
        print("Teens Tickets are $9")
    elif age < 55:
        bill = 12
        print("Adult Tickets are $12")
    elif age > 55:
        bill = 6
        print("Senior Tickets are $6")
    else:
        bill = 0
        print("You're too young to ride")

    photo_taken = input("Do you want a photo taken? Y or N ")
    if photo_taken == "Y" or photo_taken == "y":
        bill += 3
        
    print(f"Your total bill is ${bill}")
else:
    print("You're not tall enough to ride")