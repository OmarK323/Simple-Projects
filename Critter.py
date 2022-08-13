"""
Program: Initialize Critter class

Author: Omar Khan

Date: 4/26/22

"""

class Critter(object):


    def __init__ (self, name, descriptor, personalpronoun, possesivepronoun,\
            food):

        #Initialize instance variables
        self.name  = name
        self.descriptor = descriptor
        self.personalpronoun = personalpronoun
        self.possesivepronoun = possesivepronoun
        self.food = food
        self.fedcount = 0
        self.petcount = 0
        self.playcount = 0

############################################

    #Returns name of Critter, parameter is self
    def get_name(self):

        return self.name

    #Returns status of Critter, parameter is self
    def __str__(self):

        string1 = str(self.name) + " is " + str(self.descriptor)

        if (self.fedcount > 0):
            fedstr = "well-fed"
        if (self.fedcount > 2):
            fedstr = "overfull"
        if (self.fedcount == 0):
            fedstr = "hungry"

        if (self.petcount > 0):
            petstr = "happy"
        else:
            petstr = "unhappy"

        if (self.playcount > 0):
            playstr = "playful"
        else:
            playstr = "not playful"


        string2 = self.personalpronoun + " looks " + fedstr + ", " + petstr\
        + ", " + playstr

        return(string1 + ": " + string2)


    #Increases petcount by one, parameter is self
    def pet(self):

        print(self.name + " is " + self.descriptor + ", and enjoys " + \
                self.possesivepronoun + " pets!")

        self.petcount = self.petcount + 1

    #Increases fedcount by one, parameter is self
    def feed(self):

        print(self.name + " is " + self.descriptor + ", and enjoys " + \
                self.possesivepronoun + " " + self.food)

        self.fedcount = self.fedcount + 1

    #Increases playcount by one, parameter is self
    def play(self):

        print(self.name + " is " + self.descriptor + ", and enjoys " + \
                self.possesivepronoun + " playtime!")

        self.playcount = self.playcount + 1

    #Puts critter to sleep, decreasing all counters. Param is self
    def sleep(self):

        print(self.name + " is going to sleep")

        if (self.fedcount > 0):
            self.fedcount = self.fedcount - 1

        if (self.petcount > 0):
            self.petcount = self.petcount - 1

        if (self.playcount > 0):
            self.playcount = self.playcount - 1

##################################################3

def main():

    print("tests: ")

    floppy = Critter("floppy", "hoppy", "he", "his", "carrots")
    print(floppy.__str__())
    floppy.play()
    floppy.pet()
    floppy.feed()
    print(floppy.__str__())


if ((__name__) == "__main__"):

        main()


