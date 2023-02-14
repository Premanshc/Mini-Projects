import random
print('Welcome to the WORLD OFFICIAL ROCK PAPER SCISSORS CHAMPIONSHIP\n')
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice = int(input("Enter 0 for Rock and 1 for Paper and 2 for Scissors...\n"))
gameImages = [rock,paper,scissors]
print("You choice: ")
print(gameImages[user_choice])
computer_choice = random.randint(0,2)
print("Computer choice: ")
print(gameImages[computer_choice])
if user_choice >= 3 or user_choice <0:
    print("Invalid Input, please try again...")
elif user_choice==0 and computer_choice==2:
    print("You WIN!!")
elif computer_choice==0 and user_choice==2:
    print("You Lose :)")
elif computer_choice>user_choice:
    print("You Lose :)")
elif user_choice>computer_choice:
    print("You WIN!!")


