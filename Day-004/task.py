import random

#rand_num = random.randint(1, 10)

# random_number = random.random() * 10
# print(random_number)

# random_float = random.uniform(1, 10)
# print(random_float)

### Kenny's first attempt ###

# user_choice = int(input("Enter 1-5 for Heads or 6-10 for Tails "))
# computer_choice = random.randint(1, 10)
# if user_choice > computer_choice:
#     print("You win!")
# else:
#     print("Sorry, computer wins!")

### Final Product ###
heads_or_tails = random.randint(0, 1)
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")