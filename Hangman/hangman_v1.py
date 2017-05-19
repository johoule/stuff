import random

def show_start_screen():
    
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░                                                                         ░░")
    print("░░   ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █   ░░")
    print("░░  ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █   ░░")
    print("░░  ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒  ░░")
    print("░░  ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒  ░░")
    print("░░  ░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░  ░░")
    print("░░   ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ░░")
    print("░░   ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░░")
    print("░░   ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░   ░░")
    print("░░   ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░   ░░")
    print("░░                                                                         ░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░                                                                         ░░")
    print("░░                           PRESS ENTER TO PLAY                           ░░")
    print("░░                                                                         ░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

    input()


#██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
#██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
#███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
#██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
#██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
#╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝


 

def show_credits():
    print("by Jordan Houle")

def get_puzzle():
    words = ["patriots", "soccer", "camera", "the flash", "chick-fil-a", "sanic fast"]

    return random.choice(words)

def check(word, solved, guesses):
    for i in range(len(word)):
        if word[i] in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_guess():
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("invalid input, enter only a single character that is an alphabet character please.")

def display_board(solved, strikes, wrong):
    print("")
    print ("[" + wrong + "]")
    
    if strikes == 0:
        print("  +---+    ")
        print("  |   |    ")
        print("      |    ")
        print("      |    ")
        print("      |    ")
        print("      |    ")
        print(" ========= ")
    elif strikes == 1:
        print("  +---+    ")
        print("  |   |    ")
        print("  0   |    ")
        print("      |    ")
        print("      |    ")
        print("      |    ")
        print(" ========= ")
    elif strikes ==2:
        print("  +---+    ")
        print("  |   |    ")
        print("  0   |    ")
        print("  |   |    ")
        print("      |    ")
        print("      |    ")
        print(" ========= ")
    elif strikes == 3:
        print("  +---+    ")
        print("  |   |    ")
        print("  0   |    ")
        print(" /|   |    ")
        print("      |    ")
        print("      |    ")
        print(" ========= ")
    elif strikes == 4:
        print("  +---+    ")
        print("  |   |    ")
        print("  0   |    ")
        print(" /|\  |    ")
        print("      |    ")
        print("      |    ")
        print(" ========= ")
    elif strikes == 5:
        print("  +---+    ")
        print("  |   |    ")
        print("  0   |    ")
        print(" /|\  |    ")
        print(" /    |    ")
        print("      |    ")
        print(" ========= ")
    elif strikes == 6:
        print("  +---+    ")
        print("  |   |    ")
        print("  0   |    ")
        print(" /|\  |    ")
        print(" / \  |    ")
        print("      |    ")
        print(" ========= ")

    print("Word: " + solved)



def play():

    word = get_puzzle()
    solved = "*" * len(word)
    
    guesses = ""
    strikes = 0
    limit = 6
    wrong = ""

    solved = check(word, solved, guesses)
    display_board(solved, strikes, wrong)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
            strikes += 1
            wrong += letter
            

        guesses += letter
        
        solved = check(word, solved, guesses)
        display_board(solved, strikes, wrong)

    if word == solved:
        print(" ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄  ▄  ▄  ")
        print("▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌▐░▌▐░▌ ")
        print("▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌▐░▌▐░▌ ")
        print("▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌▐░▌▐░▌ ")
        print("▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌   ▄   ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌▐░▌▐░▌ ")
        print("▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌▐░▌▐░▌ ")
        print(" ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌░▌ ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌▐░▌▐░▌ ")
        print("     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌ ▀  ▀  ▀  ")
        print("     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄  ▄  ▄  ")
        print("     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌▐░▌▐░▌ ")
        print("      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀  ▀  ▀  ")
        print("")
                                                    
   
    else:
        print("▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████  ▐██▌    ")
        print(" ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀  ▐██▌    ")
        print("  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███    ▐██▌    ")
        print("  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄  ▓██▒    ")
        print("  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒ ▒▄▄     ")
        print("   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ░▀▀▒    ")
        print(" ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░  ░    ")
        print(" ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░       ░    ")
        print(" ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░ ░       ")
        print(" ░ ░                                                                    ")

    
def play_again():

    while True:
        answer = input("Play again?")

        if answer.lower() == 'no' or answer.lower() == 'n':
            return False
        elif answer.lower() == 'yes' or answer.lower() == 'y':
            return True

        print("what?!!!! Just say yes or no.")

def main():
    show_start_screen()

    again = True

    while again == True:
        
        play()
        again = play_again()

        
    show_credits()
    




# code execution begins here
if __name__ == "__main__":
    main()
