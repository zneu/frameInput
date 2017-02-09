import os
import string
import sys

def clear_screen():
    """Useses os functions to clear users screen"""
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    """Shows help"""
    # Intro message
    print "-" * 37
    print "Format your sentence -> use the keys:\n<c> Capitalize\n<u> Upper Case\n<l> Lower Case"
    print "-" * 37

def build_frame(formatted):
    """Builds frame and places formatted sentence into it"""
    # Frame variables
    sentence_length = len(formatted)
    frame_width = sentence_length + 6
    left_margin = 10
    # Builds frame using variables above. Uses algebra to print each character
    # multiple times in the shape of a frame around the formatted string.
    print
    print " " * left_margin + "+" + "-" * frame_width + "+"
    print " " * left_margin + "|" + " " * frame_width + "|"
    print " " * left_margin + "|   " + formatted + "   |"
    print " " * left_margin + "|" + " " * frame_width + "|"
    print " " * left_margin + "+" + "-" * frame_width + "+"

def get_statistics(formatted):
    """Present statistics about the users sentence"""
    print ""
    print "sentence length:", len(formatted)
    print "Checking for occurences of letters <a>, <b>, and <c>"
    sentence = formatted.lower() # lower case the string to search string for
    # occurances of 'a', 'b', 'c' [not 'A', 'B', 'C'].
    a_in_sentence = 0
    b_in_sentence = 0
    c_in_sentence = 0

    for letter in sentence:
        if letter == "a":
            a_in_sentence += 1
        elif letter == "b":
            b_in_sentence += 1
        elif letter == "c":
            c_in_sentence += 1
        else:
            pass

    if a_in_sentence == 0:
        print "There is no <a> in: " + sentence
    else:
        print "<a> occured", a_in_sentence, "times"
    if b_in_sentence == 0:
        print "There is no <b> in: " + sentence
    else:
        print "<b> occured", a_in_sentence, "times"
    if c_in_sentence == 0:
        print "There is no <c> in: " + sentence
    else:
        print "<c> occured", a_in_sentence, "times"

# Run program
clear_screen()
sentence = raw_input("Please, type a sentence.\n> ")
clear_screen()
while True:
    show_help()
    user_input = raw_input("select the format type: c, u, or l\n> ").lower()
    if user_input == "c":
        formatted = sentence.title()
        break
    elif user_input == "l":
        formatted = sentence.lower()
        break
    elif user_input == "u":
        formatted = sentence.upper()
        break
    else:
        clear_screen()
        quit = raw_input("That was not a recognized input type. Would you like to quit? y/N\n> ")
        if quit.lower() == "y":
            sys.exit("Ok, goodbyey")
        else:
            continue
clear_screen()
build_frame(formatted)
get_statistics(formatted)
