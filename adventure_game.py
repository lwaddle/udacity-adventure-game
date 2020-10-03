import os

def main():
    game_file_path = "./game_files/"

    game_model = GameModel(game_file_path)
    print(game_model._game_data)

class GameModel:
    def __init__(self, game_file_path):
        self._game_file_path = game_file_path
        self._game_data = self._load_game_data()

    def _load_game_data(self):
        """Loads the game files into a dict that uses the filename as a key
        and the actual file as a value"""
        try:
            scene_files = os.listdir(self._game_file_path)
            game_data = {}
            for file in scene_files:
                # Populate game_data dict with the filename as key
                # and the file as value.
                key = str(file).rsplit(".")[0]
                game_data[key] = file

        except:
            if os.path.isdir(self._game_file_path) == False:
                print("Error: game_file_path is invalid")
            else:
                print("Error")

        return game_data


main()