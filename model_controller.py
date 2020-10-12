import json
import os
from scene import Scene


class ModelController:
    def __init__(self, game_file_directory: str):
        self.game_data = {}
        self.game_file_directory = game_file_directory
        self._load_game_data()     # Populate the game_data dict

    def _is_valid_game_file_directory(self):
        return os.path.exists(self.game_file_directory)

    def _load_game_data(self):
        """
        Populates the game_data dict with a SceneFile object for each
        game file in the game_file directory.
        """
        if not self._is_valid_game_file_directory():
            raise Exception("Invalid game file directory")
        else:
            for file in os.listdir(self.game_file_directory):
                scene = Scene()
                if str(file).endswith("json"):
                    try:
                        with open(self.game_file_directory + file) as f:
                            json_file = json.load(f)
                            scene.scene_id = json_file["scene_id"]
                            scene.presentation_style = json_file[
                                "presentation_style"
                                ]
                            scene.print_slowly = json_file["print_slowly"]
                            scene.options_string = json_file["options_string"]
                            scene.choice_target_dict = json_file[
                                "choice_target_dict"
                                ]
                            try:
                                scene.roll_message = json_file["roll_message"]
                            except:
                                print("no roll message")
                            self.game_data[scene.scene_id] = scene
                    except:
                        raise Exception("Unable to update Scene object from JSON file.")

            for file in os.listdir(self.game_file_directory):
                if str(file).endswith("txt"):
                    try:
                        with open(self.game_file_directory + file) as f:
                            list_text = f.readlines()
                            scene_string = ""
                            for line in list_text:
                                scene_string += line

                            file_prefix = os.path.splitext(file)[0]
                            if file_prefix in self.game_data.keys():
                                tmp_scene_object = self.game_data[file_prefix]
                                tmp_scene_object.scene_string = scene_string
                                print(tmp_scene_object.scene_string)
                    except:
                        raise Exception("Unable to open game text file.")
