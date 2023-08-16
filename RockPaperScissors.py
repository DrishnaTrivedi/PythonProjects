import random
print("WELCOME TO THE GAME !!".center(150))
comp = ['rock', 'paper', 'scissor']
compPts= 0
userPts=0
while True:
    a= random.choice(comp)
    # print(f"Opponent selected {a} !")
    d = {'rock': 'paper', 'paper': 'scissor', 'scissor': 'rock'}
    print("\n")
    inp = input("Enter your Choice: rock,paper or scissor:"
                "(Enter q to quit) ")
    if(inp=='q'):
        break
    elif(d[a]==inp):
        print("its a win")
        print(f"Opponent had selected {a} !")
        userPts=userPts+1
    elif(a==inp):
        print("Its a tie")
        print(f"Opponent had selected {a} !")
    else:
        print("You Lost this one")
        print(f"Opponent had selected {a} !")
        compPts = compPts + 1
print(f"your pts :{userPts} and computer pts are {compPts}")
if(userPts>compPts):
    print("You Won the Game!!!")
elif(userPts==compPts):
    print("Its a tie!!!")
else:
    print("you lost the game")


