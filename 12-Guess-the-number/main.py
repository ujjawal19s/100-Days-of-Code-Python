#Number Guessing Game Objectives:
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
import random
# Include an ASCII art logo.
print("Welcome to the Number Guessing Game")
print("Choose a number between 1 to 100")
# Allow the player to submit a guess for a number between 1 and 100.
number = random.randint(1,101)
print(f"answer is {number}")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
if mode=="easy":
  lives =10
elif mode=="hard":
  lives = 5
print(f"You have {lives} attempts to make a guess")  

while(lives>0):
  guess = int(input("Make a guess: "))
  if guess>number:
    print("Too High")
    lives-=1
    print(f"You have {lives} attempts remaining to guess the number")
  elif guess==number:
    print(f"You got it!, the answer is {number}")
    lives=0
  else:
    print("Too Low")
    lives-=1
    print(f"You have {lives} attempts remaining to guess the number")
    
  if(lives==0 and guess!=number):
    print("You have run out of guesses, you lose")
