import os
from navigation_controller import NavigationController
from scene_controller import SceneController
from model_controller import ModelController

GAME_FILE_DIRECTORY = "./game_files/"
ROOT_SCENE_CONTROLLER_ID = "intro"

def main() -> int:
    # Instantiate the ModelController
    model_controller = ModelController(GAME_FILE_DIRECTORY)

    # Instantiate the NavigationController
    navigation_controller = NavigationController()
    
    # Instantiate the root SceneController - This is the
    # first scene in the stack.
    root_scene_controller = SceneController()
    root_scene_controller.delegate = navigation_controller
    root_scene_controller.model_controller = model_controller
    root_scene_controller.scene_id = ROOT_SCENE_CONTROLLER_ID

    return 0


main()