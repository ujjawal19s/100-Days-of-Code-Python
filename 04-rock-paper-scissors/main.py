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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if(user ==0):
  print(rock)
elif(user==1):
  print(paper)
else:
  print(scissors)

print("computer choice")
ch = random.randint(0,2)
choice = [rock,paper,scissors]
print(choice[ch])

if(user==0):
  if(ch==0):
    print("draw")
  elif(ch==1):
    print("you lose")
  else:
    print("you won")

elif(user==1):
  if(ch==0):
    print("you won")
  elif(ch==1):
    print("draw")
  else:
    print("you lose")

else:
  if(ch==0):
    print("you lose")
  elif(ch==1):
    print("you won")
  else:
    print("draw")
