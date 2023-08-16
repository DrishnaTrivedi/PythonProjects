import random
print("WELCOME TO THE DICE SIMULATOR".center(150))
list=[1,2,3,4,5,6]
d= input("Want to select the customised dice?  ")
def customise(x,y):
    weights=[20,20,20,20,20,20]
    weights[x-1]=y #100-y/5(for rest of the probabilities)
    for i in range(1,7):
        if(i==x):
            continue
        else:
            weights[i-1]=(100-y)/5
    # print(weights)
    a = random.choices(list,weights,k=1)
    print("The number on dice is : ",a)

if(d=="NO" or d=="No" or d=="no"):
    while True:
        inp= input("Enter 'r' to roll and 'q' to quit : ")
        if inp=='r':
            a= random.choice(list)
            print("The number on dice is : ",a)
        else:
            break
else:
    c, d = input("Enter the num and its probability : ").split()
    print("OK! Producing dice having prob of ", d, "for number", c)
    while True:
        inp = input("Enter 'r' to roll and 'q' to quit : ")
        if inp == 'r':
            customise(int(c),int(d))
            # a = random.choices(list, weights=(40, 30, 50, 20, 70,80),k=1)
        else:
            break






