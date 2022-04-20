import random,replit
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  
  if(sum(cards)==21 and len(cards)==2):
    return 0
    
  if 11 in cards and sum(cards)>21: 
    cards.remove(11)
    cards.append(1)
     
  return sum(cards)

def compare(user_score,computer_score):
  if user_score == computer_score :
    print("Its a Draw")
  elif(computer_score ==0):
    print("You loses")
  elif user_score == 0:
    print("You win")
  elif user_score>21:
    print("You lose")
  elif computer_score>21:
    print("You Win")
  elif user_score > computer_score:
    print("You Win")
  else:
    print("You Lose")  


def play_game():

  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False


  for n in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")


    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over = True
    else:
      choice = input("Type 'y' to draw another card or type 'n' to pass")
      if choice == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True


  while computer_score != 0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, your final score is {user_score}")
  print(f"Computer final hand is {computer_cards}, your final score is {computer_score}")
  print(compare(user_score,computer_score))



while input("Do you want to play game of blackjack? type 'y' or 'n' ")=="y":
  replit.clear()
  
  play_game()
  
