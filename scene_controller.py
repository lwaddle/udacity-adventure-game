from model_controller import ModelController


class SceneController():
    def __init__(self):
        self.delegate: id
        self.model_controller: ModelController
        self.presentation_style: str    # default or dice
        self.scene_id: str
        self.scene_main_message: str
        self.print_slowly: bool

    def dismiss_scene(self, scene_controller_to_dismiss=None):
        """
        Removes scene from view hierarchy
        """
        self.delegate.dismiss_scene(self)

    def present_scene(self, scene_controller_to_present=None):
        """
        Adds scene to view hierarchy
        """
        self.delegate.present_scene(self)

    def print_scene_to_console(self):
        # TODO
        pass
