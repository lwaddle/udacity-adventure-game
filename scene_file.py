from presentation_style import PresentationStyle


class SceneFile:
    def __init__(self):
        self.choice_target_dict: dict[str : str]
        self.options_string: str
        self.presentation_style: PresentationStyle
        self.scene_id: str
        self.scene_string: str

    # TODO