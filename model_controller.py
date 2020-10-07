import os
from scene_file import SceneFile


class ModelController:
    def __init__(self, game_file_directory: str, game_file_section_tags: list):
        self.game_data: dict[str : SceneFile]
        self.game_file_directory = game_file_directory
  ##### TODO ########## Think about how to parse the game files #####
        self.game_file_section_tags = game_file_section_tags        #
  ###################################################################
        self._load_game_data()     # Populate the data_store dict

    def _is_valid_game_file_directory(self):
        return os.path.exists(self.game_file_directory)

    def _list_sections_of_game_file(self) -> list:
        pass
    
    def _load_game_data(self):
        """
        Populates the game_data dict with a SceneFile object for each
        game file in the game_file directory. Game files are text files that
        use special tags that can be parsed for scene information. See readme.txt
        TODO - Write documentation for game file usage in readme.txt
        """
        if self._is_valid_game_file_directory():
            text_file_names = os.listdir(self.game_file_directory)
            text_file_paths = []    # This is a list of the full paths to each game text file
            for file_name in text_file_names:
                full_path = self.game_file_directory + file_name
                if os.path.isfile(full_path):
                    text_file_paths.append(full_path)
                else:
                    raise Exception("Error: Invalid file path or name")
            
            # TODO - Now that text_file_paths contains all the paths to each text file
            # I need to open and parse each text file. Maybe a seperate object or method can 
            # handle this operation. Produce a SceneFile object for each text file
            # and store it in self.game_data using the scene_id as key

            for text_file in text_file_paths:
                with open(text_file, "r") as f:
                    scene = SceneFile()
                    scene.scene_id = os.path.splitext((os.path.split(text_file)[1]))[0] # Get just the filename
                    print(scene.scene_id)
                    

        else:
            raise Exception("Error: Game file directory is invalid.")
        # TODO

