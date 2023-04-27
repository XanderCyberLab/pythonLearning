# Age Calculator

age = input("Please enter your age ")
print(age)
int_age = int(age)
days = 365 * int_age
weeks = 52 * int_age
months = 12 * int_age
print(f"You total live span in days are {days}, in weeks {weeks}, and in months {months}")