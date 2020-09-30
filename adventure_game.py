import dice
import sys
from time import sleep

MESSAGE_PAUSE_LENGTH = 1
SLOW_TEXT_SPEED = 0.01

def message_pause():
    sleep(MESSAGE_PAUSE_LENGTH)

def print_scenario(scenario, option_1, option_2 = "", option_3 = ""):
    # TODO
    return

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


test = """You discover a responsive website that looks beautiful on both mobile and desktop devices.\
You spend some time clicking around and come across the Udacity Program Catalog.\
There are so many programs! You have an interest in two of the programs - \
Full Stack Developer and iOS Developer. To help you decide which route to take, you roll a pair of dice.\
If the sum of the to dice is even, become a Full Stack Developer. If the sum of the dice is odd, \
become an iOS Developer."""

print_slowly(test)