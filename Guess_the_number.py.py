import random
randNum = random.randint(1, 100)
userguess = None
guess=0

while(userguess!=randNum):
    userguess= int(input("enter ur guess: "))
    guess+=1

    if (userguess==randNum):
        print("u guessed it right!!")
    else:
        if(userguess<randNum):
            print("u guessed it wrong, enter the larger no.")
        else:
            print("u guessed it wrong,enter the smaller no.")

print(f"u guessed the no. in {guess} guesses")

with open ("highscore.txt") as f:
    highscore= int(f.read())

if (guess>highscore):
    print("you broke the highscore!!")
with open("highscore.txt", "w") as f:
    f.write(str(guess))