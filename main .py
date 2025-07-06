#rock,paper , scissor
import random
'''
1 for rock
 -1 for paper
 0 for scissor
 '''
computer = random.choice([-1, 1, 0])
youstr = input("enter your choice:")
youdict = {"r": 1, "p": -1,"s": 0}
reversedict = {1: "roke", -1: "paper", 0: "scissor"}

you = youdict[youstr]

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer == you):
    print("it is a draw")

else:    
  if(computer ==-1 and you ==1):
     print("you lose!")

  elif(computer ==-1 and you ==0):
     print("you win!")     

  elif(computer ==1 and you ==0):
     print("you lose!")

  elif(computer ==0 and you ==1):
     print("you win!")

  elif(computer ==1 and you ==-1):
     print("you win!")

  elif(computer ==0 and you ==-1):
     print("you lose!")

  else:
     print("something was wrong")     

