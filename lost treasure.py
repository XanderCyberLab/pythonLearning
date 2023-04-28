# You're an adventurer searching for a lost treasure that's been 
# rumored to be hidden deep in the jungle. You have a map that you 
# believe will lead you to the treasure. As you journey through the 
# dense jungle, you come across a fork in the path. The map indicates 
# that the treasure could be on either path. Do you:

# 1) Take the path to the left
# 2) Take the path to the right

print("Welcome to Lost Treasure")
game_run = True

while game_run == True:
    print("You\'re an adventurer searching for a lost treasure that\'s been rumored to be hidden deep in the jungle. You have a map that you believe will lead you to the treasure. As you journey through the dense jungle, you come across a fork in the path. The map indicates that the treasure could be on either path. Do you: ")

    first_choice = int(input("1) Take the path to the left\n2) Take the path to the right"))

    if first_choice == 1:
        print("The path winds deeper into the jungle until you come across a rickety old bridge over a deep ravine. The map indicates that the treasure is on the other side. Do you: ")
        second_choice = int(input("1) Cross the bridge\n2) Turn back and take the other path"))    
        if second_choice == 1:
            print("You carefully cross the bridge, but as you reach the other side, you trigger a trap and a large pit opens up beneath your feet. You fall into the pit and are unable to climb out. Unfortunately, this is the end of your adventure.")
            game_run = False
        else:
            print("You decide to find another way around the ravine. You follow the river upstream and find a shallow spot where you can cross. As you continue down the path, you come across a hidden temple. The map indicates that the treasure is inside. Do you: ")
            third_choice = int(input("1) Enter the temple\n2) Continue down the path"))
            if third_choice == 1:
                print("You enter the temple and find yourself in a large room with multiple doors. Each door has a different symbol on it. The map indicates that the treasure is behind one of the doors, but the symbol is not clear. Do you: ")
                fourth_choice = int(input("1) Choose the door with the snake symbol\n2) Choose the door with the sun symbol\n3) Choose the door with the moon symbol"))
                if fourth_choice == 1:
                    print("You open the door with the snake symbol and find yourself face-to-face with a giant snake guarding the treasure. Do you: ")
                    fifth_choice = int(input("1) Fight the snake\n2) Run away"))
                    if fifth_choice == 1:
                        print("You defeat the snake and claim the treasure. Congratulations! You win!")
                    else:
                        print("You run away and never to be seen again. Unfortunately, this is the end of your adventure.")
                        game_run = False
                elif fourth_choice == 2:
                    print("The door opens up and a ray of sunlight shines down on you and burns you to a crisp. Unfortunately, this is the end of your adventure.")
                    game_run = False
                else:
                    print("The door opens up and coldest breeze flows out of the room. You are frozen solid. Unfortunately, this is the end of your adventure.")
                    game_run = False
            else:
                print("You get lost in the jungle and are unable to find your way back to the path. Unfortunately, this is the end of your adventure.")
                game_run = False  
    else:
        print("The path travels deep into the jungle to never been seen again. Unfortunately, this is the end of your adventure.")
        game_run = False