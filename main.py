print("Hello Alexander")

# Age Calculator

# age = input("Please enter your age ")
# print(age)
# int_age = int(age)
# days = 365 * int_age
# weeks = 52 * int_age
# months = 12 * int_age
# print(f"You total live span in days are {days}, in weeks {weeks}, and in months {months}")

# Tip Calculator

# print("Welcome to Tip Calculator.")
# total = input("What's the total cost?")
# pplPaying = input("Bill will be split in how many ways?")
# tip = input("Tip 15%, 18%, 20%?")
# float_total = float(total)
# int_pplPaying = int(pplPaying)

# if tip == str(15):
#     results = round(float_total * 1.15, 3)
# if tip == str(18):
#     results = round(float_total * 1.18, 3)
# if tip == str(20):
#     results = round(float_total * 1.20, 3)
# else:
#     print("Please try again")
    
# results /= int_pplPaying
# print(f"Total pay for each person is {results}")

print("Welcome to Tip Calculator.")
total = float(input("What's the total cost?"))
pplPaying = int(input("Bill will be split in how many ways?"))
tip = int(input("Tip 15%, 18%, 20%?"))

bill = tip / 100 * total + total
bill /= pplPaying
print(f"Total pay for each person is {bill}")