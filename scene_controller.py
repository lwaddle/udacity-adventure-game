from model_controller import ModelController
from scene import Scene


class SceneController():
    def __init__(self):
        self.delegate: id
        self.model_controller: ModelController
        self.scene: Scene

    def get_user_input(self) -> str:
        user_input = ""
        while True:
            print(self.scene.options_string)
            user_input = input(": ")
            if user_input in self.scene.choice_target_dict.keys():
                break
        
        return user_input

    def next_scene_for_user_input(self, user_input: str) -> Scene:
        target = self.scene.choice_target_dict[user_input]
        return self.model_controller.game_data[target]

    def print_scene_to_console(self):
        # TODO
        print(self.scene.scene_string)
        user_input = self.get_user_input()

        #self.delegate.push_scene_controller(self.next_scene_for_user_input(user_input))
