import random
number = random.randint(1,200)
win = False
attempts =0
print("hit!",number)
while win==False:
    guess = int(input("enter your guess: "))
    attempts +=1
    if guess == number:
        print("You won")
        print("Number of attemps: ",attempts)
        break
    else:
     if number>int(guess):
        print("Your Guess was low, Please enter a higher number")
     else:
        print("your guess was high, please enter a lower number")