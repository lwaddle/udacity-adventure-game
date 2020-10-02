import dice
import sys
import csv
from time import sleep

MESSAGE_PAUSE_LENGTH = 1
SLOW_TEXT_SPEED = 0.01

current_scene = 0   # Used as reference for scene text files

def control_scene_flow(current_scene: int):
    scene_file_path = "./scenes/" + str(current_scene) + "_scene.txt"
    options_file_path = "./scenes/" + str(current_scene) + "_options.txt"
    options_map_path = "./scenes/" + str(current_scene) + "_options_map.csv"
    
    display_scene(scene_file_path)
    decision = get_decision(options_file_path)

    map_dict = {}
    with open(options_map_path) as f:
        map = csv.DictReader(f)
        map_dict = next(map)
    
    print(map_dict)

    # TODO
    # if current_scene == 99: # Recursive base case
    #     print("fjas;lfjas;lfjasdf;lkj") # Exit the function and print some sort of exit message
    # else:
    #     clear_screen()
    #     control_scene_flow(current_scene)   # Use recursion to stack the function


def clear_screen():
    print("\n" * 500)

def display_intro():
    clear_screen()
    print("""
  __  __   __         _ __         ___     __              __              
 / / / /__/ /__ _____(_) /___ __  / _ |___/ /  _____ ___  / /___ _________ 
/ /_/ / _  / _ `/ __/ / __/ // / / __ / _  / |/ / -_) _ \/ __/ // / __/ -_)
\____/\_,_/\_,_/\__/_/\__/\_, / /_/ |_\_,_/|___/\__/_//_/\__/\_,_/_/  \__/ 
                         /___/                                             
    """)
    print("\n" * 3)

def message_pause():
    sleep(MESSAGE_PAUSE_LENGTH)

##################################################################
# This idea will probably work but now I need to change          #
# the print_slowly function because the txt files will have      #
# there own newlines. This simplifies the print_slowly function  # 
##################################################################
def display_scene(scene_txt_file):
    with open(scene_txt_file, "r") as current_scene:
        for line in current_scene:
            print_slowly(line)
    # TODO
    return

def get_decision(options_txt_file):
    with open(options_txt_file, "r") as options:
        print("\n") # Give a little space between scence and options
        lines = options.readlines()
        for line in lines:
            print(line.strip())
        option_count = len(lines)
        message = ": "
        invalid_message = "Invalid. Try again: "
        while True:
            decision = input(message)
            if decision.isdigit() == True:
                decision = int(decision)
                if decision in range(1, option_count + 1):
                    break
                else:
                    message = invalid_message
            else:
                message = invalid_message


        return decision


def print_slowly(text, pause_sentences = True):
    """Creates a classic scroll effect on the text as it prints to the screen"""
    for c in text:
        if c == "\n":
            if pause_sentences == True:
                message_pause()
        print(c, sep='', end='', flush=True); sleep(SLOW_TEXT_SPEED)





display_intro()
control_scene_flow(0)