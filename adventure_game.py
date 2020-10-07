def main() -> int:
    return 0


class SceneViewController(object):
    def __init__(self):
        self.choice: str
        self.id: str
        self.message: str
        self.scene_views: list[SceneView]
        self.target: SceneViewController

    def present_scene_view(self, scene_view: SceneView):
        pass

    def dismiss_scene_view(self, delegate):
        pass


class SceneView(object):
    def __init__(self):
        self.id: str


main()