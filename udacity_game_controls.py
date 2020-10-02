from time import sleep

class Scene:

    _scene_count = 0    # Class var to count scenes

    def __init__(self):
        Scene._scene_count += 1
        self.id = None  # int when initialized
        self.scene_string = ""
        self.options_list = []

    def print_scene_id(self):
        print(self.id)

    def scene_count(self):
        return Scene._scene_count

class SceneController:

    def __init__(self):
        self.scenes = {}        # TODO The scenes dict should be completely populated when the program runs
        self.current_scene = [] # Stack of scenes that allows user to go backwards

    def add_scene(self, scene: Scene):
        self.scenes[scene.id] = scene

    def create_scene_from_file(self, txt_file_path: str):
        with open(txt_file_path) as file:
            imported = file.readlines()
            index = 0
            id_index = 0
            start_scene_index = 0
            end_scene_index = 0
            start_options_index = 0
            end_options_index = 0
            
            while index < len(imported):
                if imported[index].startswith("@start_id"):
                    id_index = index + 1

                if imported[index].startswith("@start_scene@"):
                    start_scene_index = index + 1
                
                if imported[index].startswith("@end_scene@"):
                    end_scene_index = index - 1
                
                if imported[index].startswith("@start_options@"):
                    start_options_index = index + 1
                
                if imported[index].startswith("@end_options@"):
                    end_options_index = index - 1
                
                index += 1

            scene_id = imported[id_index]

            scene_string = ""
            for line in imported[start_scene_index : end_scene_index + 1]:
                scene_string += line

            options_list = []
            for line in imported[start_options_index : end_options_index + 1]:
                line = line.strip()
                options_list.append(line)

            # TODO
            # Add targets to the text file with the same type of format as above
            # Each scene should have a unique id so it's possible to return to
            # a previous scene once started

            scene = Scene()
            scene.id = int(scene_id)
            scene.scene_string = scene_string
            scene.options_list = options_list
            # target and id will go here

            return scene
        
    def _handle_options():


    
    def print_scene(self, scene: Scene, print_slowly=True):
        """Prints the entire scene with options"""
        text_effect_controller = TextEffectController()
        scene_string = scene.scene_string
        
        # Print the main text of the scene
        if print_slowly == True:
            text_effect_controller.print_slowly(scene_string)
        elif print_slowly == False:
            print(scene_string)

        # This is where I will put an options handler
        # TODO Options handler


class TextEffectController:
    pause_length = 1            # Time in seconds used when _pause() is called
    slow_text_speed = 0.01      # Smaller number makes text print faster when print_slowly() is called

    def print_slowly(self, text, pause_sentences=True):
        """Creates a classic scroll effect on the text as it prints to the screen"""
        for c in text:
            if c == "\n":
                if pause_sentences == True:
                    self._pause()

            print(c, sep='', end='', flush=True)
            sleep(self.slow_text_speed)

    def _pause(self):
        sleep(self.pause_length)
        