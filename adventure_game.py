import os


def main():
    game_file_dir_rel_path = "./game_files/"
    game_model = GameModel()
    game_model.game_file_dir_rel_path = game_file_dir_rel_path
    game_model.load_scene_store()           # Load up all the scene objects from the text files
    scene_controller = SceneController(game_model, "0")

    print(game_model.scene_store)

class GameModel:
    def __init__(self):
        self.game_file_dir_rel_path = ""    # Relative path to game text files
        self.scene_store = {}               # Dict that holds all the scene objects. Key string is the text file prefix.
    
    def load_scene_store(self):             # Populates the scene_store dict with scene objects. Key string is the text file prefix
        scene_store = {}
        for game_file in self._list_game_text_file_paths():
            scene = self._create_scene_from_text_file(game_file)
            scene_store[scene.scene_id] = scene
        self.scene_store = scene_store

    def _create_scene_from_text_file(self, text_file_path):         # This helper method is called by load_scene_store()
        """Parses the tags in a game file to return a scene object"""
        scene = Scene()
        # Open a text file, read using readlines(), populate scene object
        game_file_list = []
        with open(text_file_path, "r") as f:
            game_file_list = f.readlines()
        # Parse for scene_id
        scene.scene_id = self._parse_for_string_between_tags(game_file_list, "@start_scene_id@", "@end_scene_id@")
        # Parse for scene_string
        scene.scene_string = self._parse_for_string_between_tags(game_file_list, "@start_scene_string@", "@end_scene_string@")
        # Parse for options_string
        scene.options_string = self._parse_for_string_between_tags(game_file_list, "@start_options_string@", "@end_options_string@")
        # Parse for options_dict
        scene.choice_dict = self._parse_for_dict_between_tags(game_file_list, "@start_choice_dict@", "@end_choice_dict@")
        # Will return a scene object
        return scene
    

    def _list_game_text_file_paths(self):                           # This helper method is called by _create_scene_from_text_file
        """Returns a list of the text files in the game directory"""
        game_text_file_paths = []
        if os.path.isdir(self.game_file_dir_rel_path):
            text_files = os.listdir(self.game_file_dir_rel_path)
            for file in text_files:
                full_path = self.game_file_dir_rel_path + file
                if os.path.isfile(full_path):
                    game_text_file_paths.append(full_path)
                else:
                    raise Exception("Error: Invalid game file")
        else:
            raise Exception("Error: Invalid game_file path")
        return game_text_file_paths

    def _parse_for_dict_between_tags(self, list_of_lines, start_tag, end_tag):
        """Returns a dict of the text between @tags@ in a
        game file. The list_of_lines parameter is a list that's
        produced from the readlines() function on a file. The
        dict key and values are from the items in the text file that
        are separted by a space inside the @options_string@ tags"""
        output_dict = {}
        output_start_index = 0
        output_end_index = 0
        index = 0
        while index < len(list_of_lines):
            if start_tag in list_of_lines[index]:
                output_start_index = index + 1
            if end_tag in list_of_lines[index]:
                output_end_index = index - 1
            index += 1

        for line in list_of_lines[output_start_index : output_end_index + 1]:
            clean_value = str(line).strip()
            dict_values = str(clean_value).split(" ")
            if len(dict_values) > 2:
                raise Exception("Error: too many options for choice_dict")
            for line in dict_values:
                output_dict[dict_values[0]] = dict_values[1]
        return output_dict
    
    def _parse_for_string_between_tags(self, list_of_lines, start_tag, end_tag):
        """Returns a string of the text between @tags@ in a
        game file. The list_of_lines parameter is a list that's
        produced from the readlines() function on a file"""
        output_string = ""
        output_start_index = 0
        output_end_index = 0
        index = 0
        while index < len(list_of_lines):
            if start_tag in list_of_lines[index]:
                output_start_index = index + 1
            if end_tag in list_of_lines[index]:
                output_end_index = index - 1
            index += 1
        
        for line in list_of_lines[output_start_index : output_end_index + 1]:
            output_string += line

        return output_string.strip()


class Scene:
    def __init__(self):
        self.choice_dict = {}
        self.options_string = ""
        self.scene_id = ""
        self.scene_string = ""


class SceneController:
    def __init__(self, game_model: GameModel, root_scene: str):
        self.game_model = game_model
        self.root_scene = self._get_scene_with_scene_id(root_scene)    # First scene object in the stack - welcome screen
        self.scenes = []    # Stack of scene objects
        
        # Push the root scene to the scene stack
        self._push_scene(self.root_scene)

    def _get_scene_with_scene_id(self, scene_id: str):
        return self.game_model.scene_store[scene_id]
    
    def _push_scene(self, scene: Scene):
        self.scenes.append(scene)
    
    def _push_scene_with_scene_id(self, scene_id: str):
        self.scenes.append(self._get_scene_with_scene_id(scene_id))

    def print_scenes(self):
        print(self.scenes)

    
main()
