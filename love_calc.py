print("Welcome to the Love Calculator")
name_one = input("Please enter your name: ").lower()
name_two = input("Please enter your partner's name: ").lower()
t = name_one.count("t")
r = name_one.count("r")
u = name_one.count("u")
e = name_one.count("e")
total_one = (t+r+u+e)
l = name_two.count("l")
o = name_two.count("o")
v = name_two.count("v")
e = name_two.count("e")
total_two = (l+o+v+e)

score = int(str(total_one) + str(total_two))

if score > 10 or score < 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")

 