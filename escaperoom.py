"""
Author: Madison Winzeler
Description: Simple escape room game where the user is able to search a few rooms for clues to a 3-digit escape code.
"""

import sys
import json
import random
import string

# defining the 3 random numbers
def random_number():
    a = random.sample(range(10),3)

    with open('random.json', "w") as fin:
        json.dump(a, fin)
        return(a)

# identifying the first number
def kitchen_num():
    with open('random.json', "r") as fout:
        k = json.load(fout)
        kitchen = str(k[0])
        return(kitchen)

# identifying the 2nd number
def library_num():
    with open('random.json', "r") as fout:
        l = json.load(fout)
        library = str(l[1])
        return(library)

# identifying the 3rd number
def family_num():
    with open('random.json', "r") as fout:
        f = json.load(fout)
        family = str(f[2])
        return(family)

# this is the 3 numbers in a list as 1 number in order to validate the users 3 digit input response
def answer():
    with open('random.json', "r") as fout:
        a = json.load(fout)
        number = int(str(a[0]) + str(a[1]) + str(a[2]))
        return(number)

# these are the instructions
def print_instructions():
    print("Welcome to the escape room game, below are the rooms you can search to try and escape!")
    print("  Usage:")
    print("    To get more information or help:")
    print("         python escaperoom.py -i")
    print("    To search the kitchen:")
    print("         python escaperoom.py -k")
    print("    To search the library room:")
    print("         python escaperoom.py -l")
    print("    To search the family room:")
    print("         python escaperoom.py -f")
    print("    To escape with the code:")
    print("         python escaperoom.py -e")

def print_error():
    print("ERROR: Invalid command line arguments!")

# this is the main program
def main():
    if len(sys.argv)==2 and sys.argv[1]=='-i': # if only two arguments this can only be help, so if we don't have -i then we have incorrect input
        print("The number will be between 100 and 999 and will be randomly generated each time when the user enters: python escaperoom.py.")
        print("You will need to search all three rooms in order to find the 3 numbers in order to escape.")
        print_instructions()
    elif len(sys.argv) == 1:
        random_number()
        print_instructions()
    elif len(sys.argv)==2 and sys.argv[1]=='-k': # the user has chosen to search the kitchen.
        print("You have chosen to search the kitchen. In the kitchen you see that there is a clock with the number >>" + str(kitchen_num()) + "<<. (This is your first number)")
    elif len(sys.argv)==2 and sys.argv[1]=='-l': # the user has chosen to search the library
        print("As you enter the library, you see that there is a shelf missing all of the books except for one.  As you approach the lone book, you notice that it has the number >>" + str(library_num()) + "<< carved into the book. (This is your 2nd digit)")
    elif len(sys.argv)==2 and sys.argv[1]=='-f': # the user has chosen to search the family room
        print("You have entered the family room. Nothing looks out of the ordinary, but as you are about to leave the room, you notice that the two chairs and couch are arranged in the orientation of the number >>" + str(family_num()) + "<<!. (This is your FINAL number)")
    elif len(sys.argv)==2 and sys.argv[1]=='-e': # the user has chosen to search the kitchen.
        print("If you have taken the time to search all the rooms, you will now be able to figure out the escape combination, which is the concatination of the numbers.")
        userInput = int(input("Please enter your guess: "))
        if userInput == answer():
            print("Congratulations you have escaped!")
        else:
            print("I am sorry, but it looks like you are going to die alone!")
    else:
        print_error()
        print_instructions()

main()