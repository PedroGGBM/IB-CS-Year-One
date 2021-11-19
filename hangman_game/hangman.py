
"""   
    IB CS Hangman simple game 
        Pedro G IB Year 1
"""

import random
import string

def display_word(mystery_word, correct_attempts):
    # original blank word with all underscores:
    word = []
    for i in range(len(mystery_word)):
        word.append("_")
    # switches out underscores (redefining via lists) for correct attempts and their position relative to mystery_word's index
    for i in range(len(mystery_word)):
        for j in correct_attempts:
            if mystery_word[i] == j:
                word[i] = j
    return ' '.join(word)

def remaining_letters(all_attempts):
    all_letters = []
    # creates a list of all lowercase letters in an alphabet to keep track of remaining letters (to guess)
    for i in range(97, 123):
        all_letters.append(chr(i))
    # removes attempts from the choices (remaining alphabetic letters)
    for i in all_attempts:
        all_letters.remove(i)
    return ' '.join(all_letters)

def correct_guess(mystery_word, correct_attempts):
    if len(correct_attempts) == len(mystery_word): # if there are the same amount of correct attempts as # of letters in mystery_words, the word was guessed correctly
        return True
    else:
        return False

def figure(mistakes): # visual aspect of hangman (prints out ascii artwork respective to # of mistakes)
    if mistakes == 0:
        return ("    \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "=====\n")

    elif mistakes == 1:
        return ("  +  \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "=====\n")
    
    elif mistakes == 2:
        return ("  +----=+ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "=====\n")

    elif mistakes == 3:
        return ("  +-----+ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "=====\n")

    elif mistakes == 4:
        return ("  +-----+ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "=====\n")

    elif mistakes == 5:
        return ("  +-----+ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |      \n"
                "  |      \n"
                "=====\n")

    elif mistakes == 6:
        return ("  +-----+ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |     | \n"
                "  |        \n"
                "=====\n")

    elif mistakes == 7:
        return ("  +-----+ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |        \n"
                "=====\n")

    elif mistakes == 8:
        return ("  +-----+ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "=====\n")

def rand_word(): # chooses a random word from words_hangman.txt
    """ The following file words_hangman.txt is set to my directory, to run it (with the words document installed in the same directory) simply
    copy the directory name and replace the one below"""

    my_file = open(r"C:\Users\Pedro Gronda\Desktop\Python3.8\IB_CS\indv_projects\finapi_database\words_hangman.txt","r")
    lines = my_file.readlines()
    my_file.close()
    
    return(random.choice(lines).lower().strip()) # gets rid of the spaces and makes the word lowercase for convinience

def hangman(mystery_word, mistakes_allowed, figure):
    ascii_art = "\n●▬▬▬▬๑۩۩๑▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬●\n"
    mistakes = 0 # keeps count of total mistakes
    all_attempts = [] # keeps count of total attempts (for choice filtering)
    correct_attempts = [] # keepts count of total correct attempts (to see if player wins)
    
    print(f"I am thinking of a word with {len(mystery_word)} letters\nYou have {mistakes_allowed} guesses, good luck!")
    print(figure(mistakes))
    
    while mistakes < mistakes_allowed: # as long as mistakes are less than what is allowed...
        
        if correct_guess(mystery_word, correct_attempts):
            print("\nYou Win!")
            return 
        
        else:
            print(f"\nYou have {mistakes_allowed - mistakes} guesses remaining")
            print(f"Remaining letter choices: {remaining_letters(all_attempts)}")
            attempt = str(input("Enter a letter: "))
            
            if attempt in mystery_word and attempt not in all_attempts: # if the guess isn't repeated and it's in the mystery word:
                all_attempts.append(attempt)
                correct_attempts.append(attempt)
                print(figure(mistakes))
                print(f"Correct guess!\nThis is my word: {display_word(mystery_word,correct_attempts)}\n")

            elif attempt in all_attempts: # if it's already guessed it won't do unnecessary operations:
                print(f"You have already guessed that!\nThis is my word: {display_word(mystery_word,correct_attempts)}\n")
            
            else: # if the guess is incorrect:
                mistakes += 1
                print(figure(mistakes))
                all_attempts.append(attempt)
                print(f"Wrong guess!\nThis is my word: {display_word(mystery_word,correct_attempts)}\n")
    
    print(f"You Lose! The word was: {mystery_word}\n{ascii_art}")

def main(rand_word, hangman, figure):
    ascii_art = "\n●▬▬▬▬๑۩۩๑▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬●\n"
    x = "y" # initializes to pass through the while loop
    print(f"\n{ascii_art}\nWelcome to Hangman!")
    
    while x != "n":
        mystery_word = rand_word() # defines a random word from the list/doc
        hangman(mystery_word, 8, figure) # calls on the primary program
        x = str(input("Do you wish to play again? (y for yes, n for no): "))
    
    print("Thank you for playing!")

main(rand_word, hangman, figure)