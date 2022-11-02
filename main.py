# importing the art file.
import art
# import the collection of words.
from words import word_list
# importing the clear function.
from os import system, name
# importing the random file.
import random


# clear function to clear the console.
def clear():
    # for windows.
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix').
    else:
        _ = system('clear')
# end of clear function.


# main function.
def hangman():
    clear()
    # the logo, welcoming message, and the rules.
    print(art.logo)
    print("Welcome to HANGMAN game.")
    print("The rules of this game are pretty simple.")
    print("You will have a random word from our words collection.")
    print("You need to guess the correct letters until you guess the word.")
    print("Each time you make a wrong guess, you lose a life, and the HANGMAN draw.")
    print("If the HANGMAN draw completed, you lose the game.")
    print("----------------------------------------------------------------------------------------------")
    print()

    # generating a random word from the word_list collection and assign it to the game_word variable.
    # also, creating an empty list to push the underscore character for each letter in the game_word variable.
    game_word = random.choice(word_list).upper()
    hidden_word_list = []
    for letter in range(0, len(game_word)):
        hidden_word_list.append("_")

    # converting the list into a string to print to the user.
    hidden_word = ""
    for char in hidden_word_list:
        hidden_word += char + " "

    # declaring a variable to count number of life left for the user.
    # also printing the initial hangman draw.
    # then asking the user to guess a letter then we collect that answer into a variable.
    lives = 6
    print(art.stages[-1])
    print(f"WORD: {hidden_word}")
    user_guess = input("Guess a letter: ").upper()

    # this while loop will make sure the game will keep going until
    # either the lives is reached 0 or the user completely guess the word.
    while True:
        # if the user guessed the right letter, it will replace the underscore in the matched position.
        # otherwise the user will lose a life then guess again.
        if user_guess in game_word:
            for index, letter in enumerate(game_word):
                if user_guess == letter:
                    hidden_word_list[index] = user_guess

            hidden_word = ""
            for char in hidden_word_list:
                hidden_word += char + " "
        else:
            lives -= 1

        # if there is no more underscore, it means the user guessed the entire word and won the game.
        if "_" not in hidden_word:
            clear()
            print(art.logo)
            print(art.stages[lives])
            print("YOU WON!")
            print(f"The word was: {game_word}")
            break

        # if the user lost all the life available and the number lives is 0, then we end the game.
        if lives == 0:
            clear()
            print(art.logo)
            print(art.stages[0])
            print("YOU LOST!")
            print(f"The word was: {game_word}")
            break

        # clearing the console and printing the game again to continue the game.
        clear()
        print(art.logo)
        print(art.stages[lives])
        print(f"WORD: {hidden_word}")
        user_guess = input("Guess a letter: ").upper()

    # asking the user if they want to restart the game.
    restart = input("Do you want to play again Y or N? ").upper()

    if restart == "Y":
        hangman()
    else:
        print("Thanks for playing, GOODBYE.")
# end of the main function.


# calling the main function for the application to start.
hangman()
