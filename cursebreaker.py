"""
Program: Designed to play the game Curse Breaker, in which a sequence of runes is guessed

Author: Omar Khan

Last edited:
03-04-2022

"""
from random import choice

def main():

    print_introduction()

    rune_list = ["ansuz", "isaz", "sowilo", "hagalaz", "algiz", "ehwaz", "naudiz"]

    rndmlst = ["", "", "", ""]
    crypt = generate_code(rune_list, rndmlst)


    lstguess = []

    i = 0
    checker_guesser = 0
    num_matches = 0
    done = False
    while ( done == False ):

        print("")
        print("==========================")
        print("Turn " + str(i + 1))
        guessresult = get_guess(rune_list, lstguess)
        print("You guessed: ")
        print_runes(guessresult)

        checkerguesser = check_guess(crypt, guessresult)
        print("You had " + str(checkerguesser) + " matches")
        num_matches = num_matches + 1
        z = is_game_over(num_matches, checkerguesser)
        q = player_won(checkerguesser)
        i = i + 1

        if (z == True):

            if (q == True):

                print("Congrats, you win! The curse is broken")
                done = True

            else:

                print("Sorry, you lost. Better luck next time.")
                done = True
#This function prints the input list in a nicely formated way.

def print_runes(rune_list):

    accumstr = ""
    i = 0
    while (i < len(rune_list)):

        accumstr = accumstr + " | "
        accumstr = accumstr + rune_list[i]
        i = i + 1

    accumstr = accumstr + " | "

    print(accumstr)


#This function takes in a list of the possible runes and a number and ensures the input runes are legal

def get_rune(rune_listt, numb):

    rune_input = input("Input a rune: ")

    while (rune_input not in rune_listt):
        print(rune_input + " is not a valid rune.")
        print("Please choose from the following runes: ")
        print_runes(rune_listt)
        rune_input = input("Input a rune: ")

    return rune_input

#This function takes in a list of all possible runes and an empty one to store the user's guesses in

def get_guess(runes, guess):

    i = 1
    guess = []
    for i in range(4):

        r = get_rune(runes, i)
        guess.append(r)

    return(guess)


#This function takes in the possible runes and a list full of empty lists to generate the ranom rune sequence that the
#player will have to sole for

def generate_code(runes, code):

    i = 0
    while (code[3] == ""):

        x = choice(runes)

        while (x not in code):

            code[i] = x
            i = i + 1
    return code

#This function checks how many matches the player got with their guess

def check_guess(code, guess):

    matchcounter = 0
    for i in range(4):

        if (code[i] == guess[i]):

            matchcounter = matchcounter + 1

    return matchcounter

#Prints introduction and rules - cleans function up

def print_introduction():

    print("Welcome to Curse Breaker!")
    print("")
    print("The objective of the game is to guess the correct sequence of runes")
    print("each one only appears once in the sequence, and after guessing, you")
    print("will be told how many matches you got (right rune and right spot)")
    print("")
    print("The player has 13 turns to guess the correct sequence or they lose")

#This function tells the user when the game is over
def is_game_over(num, turn):

    if (num == 13 or turn == 4):

        return True

#Tells when player wins the game
def player_won(num):

    if (num == 4):

        return True



