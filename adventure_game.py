import os

def main():
    game_file_path = "./game_files/"
    game_model = GameModel(game_file_path)
    scene_controller = SceneController(game_model, root_scene_id="0")

    game_model.create_scene("0")

    

class GameModel:
    def __init__(self, game_file_path):
        self._game_file_path = game_file_path
        self._game_data = self._load_game_data()    # dict


    def _load_game_data(self):
        """Loads the game files into a dict that uses the filename as a key
        and the actual file as a value"""
        try:
            scene_files = os.listdir(self._game_file_path)
            game_data = {}
            for file in scene_files:
                # Populate game_data dict with the filename as key
                # and the file as value.
                key = str(file).rsplit(".")[0]  # Separate the filename from the file extension
                game_data[key] = file

        except:
            if os.path.isdir(self._game_file_path) == False:
                print("Error: game_file_path is invalid")
            else:
                print("Error")

        return game_data

    def create_scene(self, scene_id):
        pass
        # scene = Scene()

        # scene.scene_id = ""
        # with open(self._game_data[scene_id]) as f:
        #     game_file_txt = f.readlines()
        #     index = 0
        #     while index < len(game_file_txt):
        #         if "@scene_id" in game_file_txt[index]:
        #             if game_file_txt[index + 1].isascii() and game_file_txt[index + 1] != "\n":
        #                 scene_id = game_file_txt[index + 1].strip()

class Scene:
    def __init__(self):
        self.scene_id = ""
        self.scene_string = ""
        self.options_string = ""
        self.choice_dict = {}


class SceneController:
    def __init__(self, game_model, root_scene_id):
        self._game_model = game_model
        self._root_scene_id = root_scene_id
        self.current_scenes = []    # Stack of Scene objects grows as game progresses
    
    def push_scene(self, scene: Scene):
        self.current_scenes.append(scene)

    def pop_scene(self):
        self.current_scenes.pop()


main()