import random

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

# print("Player choice: ")
# if player_choice == 0:
#     print(rock)    
# if player_choice == 1:
#     print(paper)    
# if player_choice == 2:
#     print(scissors)
# print("Computer choice: ")
# if computer_choice == 0:
#     print(rock)
# if computer_choice == 1:
#     print(paper)
# if computer_choice == 2:
#     print(scissors)
images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

print("Player choice: ")
print(images[player_choice])
computer_choice = random.randint(0,2)
print("Computer choice: ")
print(images[computer_choice])



if player_choice == computer_choice:
    print("Tie!")
elif player_choice == 0:
    if computer_choice == 1:
        print("You lose! Paper covers rock.")
    else:
        print("You win! Rock smashes scissors.")
elif player_choice == 1:
    if computer_choice == 2:
        print("You lose! Scissors cut paper.")
    else:
        print("You win! Paper covers rock.")
elif player_choice == 2:
    if computer_choice == 0:
        print("You lose! Rock smashes scissors.")
    else:
        print("You win! Scissors cut paper.")
else:
    print("Invalid choice. Please enter either rock, paper, or scissors.")
    