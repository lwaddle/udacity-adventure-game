from dice import Dice
from model_controller import ModelController
from scene import Scene
from text_effect import TextEffect


class SceneController():
    def __init__(self):
        self.delegate: id
        self.model_controller: ModelController
        self.scene: Scene
        self.text_effect = TextEffect()

    def get_user_input(self) -> str:
        user_input = ""
        while True:
            print(self.scene.options_string)
            user_input = str(input(": ")).lower()
            if user_input in self.scene.choice_target_dict.keys():
                break
        return user_input

    def next_scene_for_user_input(self, user_input: str) -> Scene:
        target = self.scene.choice_target_dict[user_input]
        return self.model_controller.game_data[target]

    def print_scene_to_console(self):
        self.text_effect.clear_screen()
        if self.scene.print_slowly == True:
            self.text_effect.print_slowly(self.scene.scene_string, self.scene.print_slowly)
        else:
            print(self.scene.scene_string)
        user_input = self.get_user_input()
        target = self.scene.choice_target_dict[user_input]
        if target not in ["back", "exit"]:
            # Create a new scene controller and add it to the navigation controller
            next_scene_controller = SceneController()
            next_scene_controller.delegate = self.delegate
            next_scene_controller.model_controller = self.model_controller
            next_scene_controller.scene = self.next_scene_for_user_input(user_input)
            next_scene_controller.delegate.push_scene_controller(next_scene_controller)

        if target in ["back", "exit"]:
            if target == "back":
                self.delegate.pop_scene_controller(self)
            if target == "exit":
                self.delegate.scene_controllers = []
                self.text_effect.clear_screen()
                print(self.model_controller.game_data["exit"].scene_string)
