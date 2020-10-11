import os
from navigation_controller import NavigationController
from scene_controller import SceneController
from model_controller import ModelController

GAME_FILE_DIRECTORY = "./game_files/"
ROOT_SCENE_CONTROLLER_ID = "intro"

def main() -> int:
    # Start the game
    start_game()

    return 0

def start_game():
    # Instantiate the ModelController
    model_controller = ModelController(GAME_FILE_DIRECTORY)

    # Instantiate the NavigationController
    navigation_controller = NavigationController()
    
    # Instantiate the root SceneController - This is the
    # first scene in the hierarchy.
    root_scene_controller = SceneController()
    root_scene_controller.delegate = navigation_controller
    root_scene_controller.model_controller = model_controller
    root_scene_controller.scene = model_controller.game_data[ROOT_SCENE_CONTROLLER_ID]
    
    # Present the first scene
    root_scene_controller.delegate.push_scene_controller(root_scene_controller)

    # LOOK AT THIS CODE BELOW TO REMEBER HOW TO ADD MORE SCENE CONTROLLERS
    # # TESTING
    # #######################################
    # s1 = SceneController()
    # s1.delegate = navigation_controller
    # s1.model_controller = model_controller
    # s1.scene = model_controller.game_data["1"]
    # s1.delegate.push_scene_controller(s1)

    # print(navigation_controller.scene_controllers)

    # s1.delegate.pop_scene_controller(s1)
    # print(navigation_controller.scene_controllers)

    # #######################################
    # # TESTING
    



main()