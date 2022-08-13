"""
Program: Allows a user to interact with Critter class objects

Author: Omar Khan

Date: 04/27/2022

"""
from critter import *


def main():

    done = False
    lstcritters = [ ]
    while (done == False):
        choice = printoptions()
        if (choice == 1):
            check_room(lstcritters)
            for i in range(len(lstcritters)):
                print(lstcritters[i])
                print()
        elif (choice == 2):
            crit = create_critter()
            lstcritters.append(crit)
        elif (choice == 3):
            if (len(lstcritters) > 0):
                feed_critter(lstcritters)
            else:
                print("No critters to feed")
        elif (choice == 4):
            if (len(lstcritters) > 0):
                pet_critter(lstcritters)
            else:
                print("No critters to pet")
        elif (choice == 5):
            if (len(lstcritters) > 0):
                play_critter(lstcritters)
            else:
                print("No critters to play with")
        elif (choice == 6):
            sleep_critter(lstcritters)
        else:
            break

    game_done()

#No params or returns: prints out options and takes in user's choice
def printoptions():

    print("----------------------------")
    print("Main Menu: ")
    print("1. Check on critters")
    print("2. Add new critter")
    print("3. Feed critter")
    print("4. Pet critter")
    print("5. Play with critter")
    print("6. Go to bed")
    print("0. Quit")

    choice = int(input("Selection: "))
    print()

    lstopt = [0, 1 , 2, 3, 4, 5, 6]
    while (choice not in lstopt):

        print("invalid choice, please select again")
        choice = input("Selection: ")
        print()

    return(choice)

#param is critter list, no returns. Describes number of critters
def check_room(lstcritters):

    pop = len(lstcritters)

    if (pop >= 1):

        print("Some critters")
        print()

    elif (pop > 4):

        print("Full of critters")
        print()

    elif (pop < 1):
        print("Empty")
        print()

#
def create_critter():

    name = input("Critter name? ")
    adj = input("Critter descriptor? ")
    perpro = input("Critter personal pronoun (she, they, it, ze)? ")
    pospro = input("Critter possesive pronoun (her, their, its, zir)? ")
    food = input("Critter's favorite food? ")
    crit = Critter(name, adj, perpro, pospro, food)
    return(crit)


#
def feed_critter(lstcritters):

    crchoice = pick_critter(lstcritters)

    print()
    lstcritters[crchoice-1].feed()
    print()

#
def pet_critter(lstcritters):

    crchoice = pick_critter(lstcritters)

    print()
    lstcritters[crchoice-1].pet()
    print()
    
def play_critter(lstcritters):

    crchoice = pick_critter(lstcritters)

    print()
    lstcritters[crchoice-1].play()
    print()


#
def sleep_critter(lstcritters):

    crchoice = pick_critter(lstcritters)
    print()
    lstcritters[crchoice-1].sleep()
    print()

#
def pick_critter(lstcritters):

    lstnames = [ ]
    for i in range(len(lstcritters)):

        name1 = lstcritters[i].get_name()
        lstnames.append(name1)
        print( str(i + 1) + ". " + name1)

    crchoice = input("Pick a critter (number): ")

    while (crchoice.isnumeric() == False or int(crchoice) <= 0 or \
            int(crchoice) > len(lstcritters)):

        print("Pick an existing critter.")
        crchoice = input("Pick a critter: ")

    return(int(crchoice))


#
def game_done():

    print("Goodbye!")

main()

#
