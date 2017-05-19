# Add an import statement here so we can use the random.choice function.
import random

# Create a dictionary of 15 Spanish or French words and their English
# translations. Call the dict vocab. 
vocab = {'un' : 'one', 'deux' : 'two', 'trois' : 'three', 'quatre' : 'four',
         'cinq': 'five', 'six' : 'six', 'sept' : 'seven',  'huit' : 'eight',
         'neuf' : 'nine', 'dix' : 'ten', 'onze' : 'eleven', 'douze' : 'tweleve',
         'treize' : 'thirten', 'quatorze' : 'fourteen'}


# Start the game.
print("Let's play Flash Cards!")
right = 0


# Loop until the player gets 7 consecutive words correct.
while right < 7:
    # Create a list called spanish (or french) which contains the
    # keys from your vocab dict.
    french = list(vocab.keys())

    # Use the choice function to select a random word from the
    # list of keys. Store this word in a variable called question.
    question = random.choice(french)

    # Store the corresponding value for that key in a variable
    # called answer.
    answer = vocab[question]

    # Print the question word and prompt the user for a guess.
    guess = input('what is the english translation of ' + question + '?')

    # If guess is equal to answer, print a message stating so and
    # increase the right total by 1. Otherwise, print a message
    # telling the player the correct answer and reset right to zero.
    if guess == answer:
        print('good job!')
        right += 1
    else:
        print('nope')
        right = 0

    

    # Print the number of consecutive correct answers so far.
    print('you have a streak of ' + str(right) + ' answers.')




          
# End the game.
print("Good job. That's 7 correct answers in a row. You win!")
