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

#Write your code below this line 👇
import random
list = [rock, paper, scissors]
player_choice = int(input("What do  you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(list[player_choice])
print(f"Copmuter chose:\n{list[computer_choice]}\n")

if player_choice == computer_choice:
    print("Tie!")
elif player_choice == computer_choice + 1\
    or player_choice == 0 and computer_choice == 2:
    print("You win!")
else:
    print("You lose!")
