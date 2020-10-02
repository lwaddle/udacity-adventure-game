class Scene:

    _scene_count = 0    # Class var to count scenes

    def __init__(self):
        Scene._scene_count += 1
        self.id = 9999  # Init to dummy value.
        self.scene_string = ""
        self.options_string = ""

    def print_scene_id(self):
        print(self.id)

    def scene_count(self):
        return Scene._scene_count


class SceneController:

    def __init__(self):
        self.scenes = []

    def add_scene(self, scene: Scene):
        self.scenes.append(scene)

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
            scene_string = scene_string.strip()

            options_string = ""
            for line in imported[start_options_index : end_options_index + 1]:
                options_string += line
            options_string = options_string.strip()

            # TODO
            # Add targets to the text file with the same type of format as above
            # Each scene should have a unique id so it's possible to return to
            # a previous scene once started

            scene = Scene()
            scene.id = int(scene_id)
            scene.scene_string = scene_string
            scene.options_string = options_string
            # target and id will go here

            return scene
        

        

        