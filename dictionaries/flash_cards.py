# Add an import statement here so we can use the random.choice function.
import random

# Create a dictionary of 15 Spanish or French words and their English
# translations. Call the dict vocab. 
binary = {'32' : 'space', '33' : 'exclamation point', '34' : 'double quote',
          '35' : 'number', '36': 'dollar', '37' : 'percent', '38' : 'ampersand',
          '39' : 'single quote', '40' : 'left parenthesis', '41' : 'right parenthesis',
          '42' : 'asterisk', '43' : 'plus', '44' : 'comma', '45' : 'minus',
          '46' : 'period', '47' : 'forward slash', '48' : 'zero', '49' : 'one',
          '50' : 'two', '51' : 'three', '52' : 'four', '53' : 'five', '54' : 'six',
          '55' : 'seven', '56' : 'eight', '57' : 'nine', '58' : 'colon', '59' : 'semicolon',
          '60' : 'less than', '61' : 'equals', '62' : 'greater than', '63' : 'question mark',
          '64' : 'at symbol', '65': 'A', '66' : 'B', '67' : 'C', '68' : 'D', '69' : 'E',
          '70' : 'F', '71' : 'G', '72' : 'H', '73' : 'I', '74' : 'J', '75' : 'K',
          '76' : 'L', '77' : 'M', '78' : 'N', '79' : 'O', '80' : 'P', '81' : 'Q',
          '82' : 'R', '83' : 'S', '84' : 'T', '85' : 'U', '86' : 'V', '87' : 'W',
          '88' : 'X', '89' : 'Y', '90' : 'Z', '91' : 'open bracket', '92' : 'backslash',
          '93' : 'closing bracket', '94' : 'caret', '95' : 'underscore', '96' : 'grave accent',
          '97' : 'a', '98' : 'b', '99' : 'c', '100' : 'd', '101' : 'e', '102' : 'f',
          '103' : 'g', '104' : 'h', '105' : 'i', '106' : 'j', '107' : 'k', '108' : 'l',
          '109' : 'm', '110' : 'n', '111' : 'o', '112' : 'p', '113' : 'q', '114' : 'r',
          '115' : 's'}


# Start the game.
print("Let's play Flash Cards!")
right = 0
correct = 10


# Loop until the player gets 7 consecutive words correct.
while right < correct:
    # Create a list called spanish (or french) which contains the
    # keys from your vocab dict.
    decimal = list(binary.keys())

    # Use the choice function to select a random word from the
    # list of keys. Store this word in a variable called question.
    question = random.choice(decimal)

    # Store the corresponding value for that key in a variable
    # called answer.
    answer = binary[question]

    # Print the question word and prompt the user for a guess.
    guess = input('What ascii character does the decimal ' + question + ' represent?')
    
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
print("Good job. That's " + str(correct) + " correct answers in a row. You win!")
