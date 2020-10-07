from presentation_style import PresentationStyle
from model_controller import ModelController


class SceneController():
    def __init__(self):
        self.delegate: id
        self.model_controller: ModelController
        self.presentation_style: PresentationStyle      # TODO determine if this is a good way to display normal and dice views
        self.scene_id: str
        self.scene_main_message: str

    def dismiss_scene(self, scene_controller_to_dismiss=None):
        self.delegate.dismiss_scene(self)

    def present_scene(self, scene_controller_to_present=None):
        self.delegate.present_scene(self)

    def print_scene_to_console(self):
        # TODO
        pass
