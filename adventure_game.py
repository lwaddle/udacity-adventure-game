import dice
import sys
from time import sleep

MESSAGE_PAUSE_LENGTH = 1
SLOW_TEXT_SPEED = 0.01

def message_pause():
    sleep(MESSAGE_PAUSE_LENGTH)

##################################################################
# This idea will probably work but now I need to change          #
# the print_slowly function because the txt files will have      #
# there own newlines. This simplifies the print_slowly function  # 
##################################################################
def display_scene(scene: str):
    with open("./scenes/0.txt", "r") as current_scene:
        for line in current_scene:
            print_slowly(line)
    # TODO
    return

def get_decision(option_1, option_2 = "", option_3 = ""):
    options = 1 # increments if options 2 and 3 are used
    print(f"Press 1: {option_1}")
    if option_2:
        print(f"Press 2: {option_2}")
        options += 1
    if option_3:
        print(f"Press 3: {option_3}")
        options += 1
    
    decision = input(": ")
    if decision.isdigit() == True:
        decision = int(decision)
    while decision not in range(1, options + 1):
        decision = input("Invalid... Try again: ")
        if decision.isdigit() == True:
            decision = int(decision)

    return decision


def print_slowly(text, pause_sentences = True, line_spacing = 1):
    """Creates a classic scroll effect on the text as it prints to the screen"""
    i = 0
    while i < len(text):
        print(text[i], sep='', end='', flush=True); sleep(SLOW_TEXT_SPEED)
        if text[i] in [".", "!", ";"]:
            if pause_sentences == True:
                message_pause()
            if i < len(text) - 1 and text[i + 1] == " ":    # i < len(text) - 1 prevents index range error
                i += 1  # Skip the space after the period
            print("\n" * line_spacing)    
        i += 1


# test = """You discover a responsive website that looks beautiful on both mobile and desktop devices.\
# You spend some time clicking around and come across the Udacity Program Catalog.\
# There are so many programs! You have an interest in two of the programs - \
# Full Stack Developer and iOS Developer. To help you decide which route to take, you roll a pair of dice.\
# If the sum of the to dice is even, become a Full Stack Developer. If the sum of the dice is odd, \
# become an iOS Developer."""