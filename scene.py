from presentation_style import PresentationStyle


class Scene:
    def __init__(self):
        self.choice_target_dict: dict[str : str]
        self.options_strings: list
        self.presentation_style: PresentationStyle
        self.scene_id: str
        self.scene_string: str

    # TODO