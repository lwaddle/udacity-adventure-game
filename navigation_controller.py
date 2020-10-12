from scene_controller import SceneController


class NavigationController(SceneController):
    def __init__(self):
        self.scene_controllers = []

    def pop_scene_controller(self, scene_controller: SceneController):
        """
        Pops the top scene controller from the navigation stack and updates the display
        """
        self.scene_controllers.pop()
        scene_controller = None
        # Update the display
        if len(self.scene_controllers) >= 1:
            self.scene_controllers[-1].print_scene_to_console()
    
    def push_scene_controller(self, scene_controller: SceneController):
        """
        Adds scene to the navigation stack and updates the display
        """
        self.scene_controllers.append(scene_controller)
        # Update the display
        scene_controller.print_scene_to_console()