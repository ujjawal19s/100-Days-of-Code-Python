#modules
from art import logo,vs
from game_data import data
import random
from replit import clear

def format_data(account):
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  
  return f"{account_name}, a {account_desc}, from {account_country}"

#Check user is correct
def check_answer(guess, a_followers, b_followers):
  if (guess=="a" and a_followers>b_followers):
    return True
  elif (guess=="b" and b_followers>a_followers):
    return True
  else:
    return False
    
print(logo)
score  = 0

should_continue = True
account_b = random.choice(data)

while should_continue:
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")

  #Ask the user for choice
  guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

  #Account followers count
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']

  clear()
  print(logo)
  is_correct = check_answer(guess,a_follower_count,b_follower_count)

  if is_correct:
    score+=1
    print(f"You are right! Current score is {score}")
  else:
    should_continue = False
    clear()
    print(f"Sorry, that's wrong. Final Score is {score}")
