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
question = int(input("Type 0 for rock, 1 for paper, 2 for scissors!"))

print ("You chose:")

if question == 0:
  print (rock)
elif question == 1:
  print (paper)
elif question == 2:
  print (scissors)

aimove = random.randint(0,2)

print ("The AI chose:")

if aimove == 0:
  print (rock)
elif aimove == 1:
  print (paper)
elif aimove == 2:
  print (scissors)



if question == aimove:
  print ("It's a draw!")
elif question == 0 and aimove == 1:
  print ("You lose :(")
elif question == 1 and aimove == 0:
  print ("You win!")
elif question == 1 and aimove == 2:
  print ("You lose :(")
elif question == 2 and aimove == 1:
  print ("You win!")
elif question == 2 and aimove == 0:
  print ("You Lose:(")
elif question == 0 and aimove == 2:
  print ("You win!")
else:
  print ("Please enter a valid number.")
