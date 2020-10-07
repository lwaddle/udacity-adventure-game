from scene_controller import SceneController


class NavigationController(SceneController):
    def __init__(self):
        self.scene_controllers = []

    def dismiss_scene(self, scene_controller_to_dismiss=None):
        self.scene_controllers.pop()

    def present_scene(self, scene_controller_to_present=None):
        # Overide method here
        self.scene_controllers.append(scene_controller_to_present)
