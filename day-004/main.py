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

hand_shape = [rock, paper, scissors]
user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0,2)

if user_choice < 0 or user_choice >= 3:
    print("Invalid number. You lose.")
elif user_choice == 0 and computer_choice == 2:
    print(hand_shape[user_choice] + "\n")
    print("Computer chose:\n")
    print(hand_shape[computer_choice] + "\n")
    print("You win!")
elif computer_choice == 0 and user_choice ==2:
    print(hand_shape[user_choice] + "\n")
    print("Computer chose:\n")
    print(hand_shape[computer_choice] + "\n")
    print("You lose (whomp, whomp)")
elif computer_choice < user_choice:
    print(hand_shape[user_choice] + "\n")
    print("Computer chose:\n")
    print(hand_shape[computer_choice] + "\n")
    print("You win!")
elif user_choice < computer_choice:
    print(hand_shape[user_choice] + "\n")
    print("Computer chose:\n")
    print(hand_shape[computer_choice] + "\n")
    print("You lose (whomp, whomp)")
else:
    print(hand_shape[user_choice] + "\n")
    print("Computer chose:\n")
    print(hand_shape[computer_choice] + "\n")
    print("Draw. Please try again.")
