import random

print("Let's play a Number game!")
print("I'm thinking of a number from 1 to 100")
print("You try to guess, and I'll tell you if you're right.")

num = random.randint(1, 100)

got_it = False
limit = 6
tries = 0

while got_it == False and tries < limit:
    
    guess = input("What number am I thinking of? ")
    guess = int(guess)
    
    if guess < num:
        print("Nope. Too low.")
    elif guess > num:
        print("Nope. Too high.")
    else:
        got_it = True

    tries += 1


if got_it == True:
    print("You're a winner!")
else:
    print("You r dum")




print("Game over")
play_again = input("Play Again?")



