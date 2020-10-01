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
def display_scene(txt_file):
    with open(txt_file, "r") as current_scene:
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


def print_slowly(text, pause_sentences = True):
    """Creates a classic scroll effect on the text as it prints to the screen"""
    for c in text:
        if c == "\n":
            if pause_sentences == True:
                message_pause()
        print(c, sep='', end='', flush=True); sleep(SLOW_TEXT_SPEED)


display_scene("./scenes/0_scene.txt")