from kivy.lang import Builder
from kivymd.app import MDApp

class GamesApp(MDApp):
    def build(self):
        self.title = "Hand Games"
        self.icon = "icons/hand-games-rounded.png"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file('pages/Games/games.kv')