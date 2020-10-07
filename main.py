import os

from navigation_controller import NavigationController
from scene_controller import SceneController
from model_controller import ModelController

def main() -> int:
    # Instantiate the ModelController
    model_controller = ModelController(
        "./game_files/", 
        [
            "@start_presentation_style@",
            "@end_presentation_style@",
            "@start_scene_string@", 
            "@end_scene_string@", 
            "@start_options_string@", 
            "@end_options_string@", 
            "@start_choice_target_dict@", 
            "@end_choice_target_dict@"])

    # Instantiate the NavigationController
    navigation_controller = NavigationController()
    
    # Instantiate the root SceneController - This is the
    # first scene in the stack.
    root_scene_controller = SceneController()
    root_scene_controller.delegate = navigation_controller
    root_scene_controller.model_controller = model_controller
    root_scene_controller.scene_id = "intro"

    return 0


main()