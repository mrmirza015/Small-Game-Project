import random
i=0
while(i<5):
 def game(comp,you):
    print(f"Computer chose '{comp}' and you chose '{you}' therefore:\n")
    if(comp==you):print("Match Draw")
    if(comp=='s'):
        if(you=='w'):
            print("You lose")
        if(you=='g'):
            print("You win")
    elif(comp=='w'):
        if(you=='g'):
            print("You lose")
        if(you=='s'):
            print("You win")
    elif(comp=='g'):
        if(you=='w'):
            print("You lose")
        if(you=='s'):
            print("You win")

 randNum=random.randint(1,3)
 if(randNum==1):
    comp='s'
 elif(randNum==2):
    comp='w'
 elif(randNum==3):
    comp='g'
 i=i+1
 you=input("Enter your choice(snack(s),water(w),gun(g)): \n")

 game(comp, you)



