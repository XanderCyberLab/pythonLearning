import random
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_random = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if player_choice == "0":
    print(rock)
    
elif player_choice == "1":
    print(paper)
    
else:
    print(scissors)
    