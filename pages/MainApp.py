from kivymd.app import MDApp
from kivy.lang import Builder

from pages import HomeApp, GamesApp

def open_home(app = None):
    if app != None:
        app.stop()
    HomeApp().run()

def open_games(app):
    app.stop()
    GamesApp().run()
