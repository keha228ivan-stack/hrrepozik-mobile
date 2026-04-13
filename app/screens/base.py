from kivymd.uix.screen import MDScreen


class BaseScreen(MDScreen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
