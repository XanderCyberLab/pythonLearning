import random

# num_int= random.randint(1, 100)
# print(num_int)

# num_float= random.random() * 5
# print(num_float)

# grade_score = random.randint(1, 100)
# print(grade_score)

heads = 1
tails = 0

flipcoin = random.randint(0, 1)

if flipcoin == 1:
    print("Heads")
else:
    print("Tails")