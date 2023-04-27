bill = 0
print("Welcome to Wishymashy's Pizza Deliveries!")
num_Of_Pizzas = int(input("How many pizzas do you want? "))
size_Of_Pizza = int(input("Please Select Size of Pizza: \n 1. Small $5 \n 2. Medium $10 \n 3. Large $15\n"))
if size_Of_Pizza == 1:
    bill += 5 * num_Of_Pizzas
elif size_Of_Pizza == 2:
    bill += 10 * num_Of_Pizzas
elif size_Of_Pizza == 3:
    bill += 15 * num_Of_Pizzas
else:
    print("Please select a value option")
    
print(f"You current total is {bill}")
toppings = input("Do you want toppings? Y or N ")
if toppings == "Y" or toppings == "y":
    pepperoni = input("Do you want pepperoni for $1? Y or N ")
    if pepperoni == "Y" or pepperoni == "y":
        bill += 1 + num_Of_Pizzas
    beef = input("Do you want beef for $2? Y or N ")
    if beef == "Y" or beef == "y":
        bill += 2 + num_Of_Pizzas
    pineapple = input("Do you want pineapple for $10? Y or N ")
    if pineapple == "Y" or pineapple == "y":
        bill += 10 + num_Of_Pizzas
    print(f"Your total is ${bill}")
    
else: 
    print(f"Your total is ${bill}")
