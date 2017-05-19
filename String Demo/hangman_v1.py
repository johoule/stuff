word = "patriots"
solved = "-" * len(word)
guesses = ""

print("Let's play Hangman!")
print(solved)

while word != solved:
    guesses += input("Guess a letter: ")

    for i in range(len(word)):
        if word[i] in guesses:
            solved = solved[:i] + word[i] + solved[i+1:]

    print(solved)

print("You win!")

