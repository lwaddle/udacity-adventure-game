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

    def is_even(self, n: int) -> bool:
        if n % 2 == 0:
            return True
        return False

    def next_scene_for_user_input(self, user_input: str) -> Scene:
        target = self.scene.choice_target_dict[user_input]
        return self.model_controller.game_data[target]

    def print_scene_to_console(self):
        self.text_effect.clear_screen()
        if self.scene.print_slowly is True:
            self.text_effect.print_slowly(self.scene.scene_string,
                                          self.scene.print_slowly)
        else:
            print(self.scene.scene_string)
        if self.scene.presentation_style == "dice":
            # Roll the dice
            dice_roll = Dice()
            (die_1, die_2) = dice_roll.roll_two_dice()
            even_or_odd = ""
            if self.is_even(self.sum(die_1, die_2)):
                even_or_odd = "even"
                user_input = even_or_odd
            else:
                even_or_odd = "odd"
                user_input = even_or_odd
            print(f"\n\nYou rolled a {die_1} and a {die_2}.\n\nThe sum is " +
                  f"{self.sum(die_1, die_2)}, which is {even_or_odd}.\n\n")
            exit_loop = "."     # Dummy value.
            while exit_loop != "":
                exit_loop = input(f"Press ENTER to continue to the " +
                                  f"{self.scene.roll_message[even_or_odd]} " +
                                  f"program: ")
        else:
            user_input = self.get_user_input()
        target = self.scene.choice_target_dict[user_input]
        if target not in ["back", "exit", "new_game"]:
            # Create a new scene controller and add it
            # to the navigation controller
            next_scene_controller = SceneController()
            next_scene_controller.delegate = self.delegate
            next_scene_controller.model_controller = self.model_controller
            next_scene_controller.scene = \
                self.next_scene_for_user_input(user_input)
            next_scene_controller.delegate.\
                push_scene_controller(next_scene_controller)

        if target in ["back", "exit", "new_game"]:
            if target == "back":
                self.delegate.pop_scene_controller(self)
            if target == "exit":
                self.delegate.scene_controllers = []
                self.text_effect.clear_screen()
                print(self.model_controller.game_data["exit"].scene_string)
            if target == "new_game":
                tmp_root_scene_controller = self.delegate.scene_controllers[0]
                self.delegate.scene_controllers = []
                self.text_effect.clear_screen()
                self.delegate.push_scene_controller(tmp_root_scene_controller)

    def sum(self, a, b):
        return a + b
