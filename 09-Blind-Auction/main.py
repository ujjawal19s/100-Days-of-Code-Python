from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
bidders = {}

def find_highest_bidder(bidding_record):
  winner=""
  max = 0
  for key in bidding_record:
    if(bidding_record[key]>max):
      max = bidding_record[key]
      winner = key

  print(f"The winner is {winner} with amount of ${max}")
  
  
should_continue = True
while(should_continue):

  name = input("enter your name: ")
  amount = int(input("enter the amount you bid: $"))
  bidders[name] = amount

  result = input("do you want to continue? type yes or no ")
  
  if(result =="no"):
    should_continue = False
    find_highest_bidder(bidders)
  elif(result =="yes"):
    clear()
