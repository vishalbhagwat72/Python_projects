import random 

def game(comp, you):
    if comp==you:
        return None

    elif comp=="r":
        if you=="p":
            return True
        elif you=="s":
            return False

    elif comp=="p":
        if you== "s":
            return True
        elif you=="r":
            return False
    
    elif comp== "s":
        if you== "p":
            return False
        elif you== "r":
            return True

print("computers turn: rock(r) paper(p) scieser(s)?")
randomNum= random.randint(1, 3)

if randomNum== 1:
    comp="r"

elif randomNum==2:
    comp="p"

elif randomNum==3:
    comp="s"

you= input("yours choise: rock(r) paper(p) scieser(s)?")

a= game(comp, you)

print("comp selects: "+ str(comp) )
print("you selects: "+str(you))

if a==None:
    print("its tie")

elif a:
    print("you win!")

else:
    print ("you loose!")