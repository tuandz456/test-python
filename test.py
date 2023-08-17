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
c = [rock, paper, scissors]
a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
import random
b = random.randint(0, 2)
print(c[a] + "\n Computer chose:" + c[b])
if a == b -2 or a == b + 1:
  print("You Win")
elif a == b:
  print("Hoa")
else:
  print("You loose")


