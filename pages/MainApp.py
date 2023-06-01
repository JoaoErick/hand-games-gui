from kivymd.app import MDApp
from kivy.lang import Builder

from pages import HomeApp, GamesApp, JokenpoApp, EvenOddApp, NearestNumberApp

def open_home(app = None):
    if app != None:
        app.stop()
    HomeApp().run()

def open_games(app):
    app.stop()
    GamesApp().run()

def open_jokenpo(app):
    app.stop()
    JokenpoApp().run()

def open_even_odd(app):
    app.stop()
    EvenOddApp().run()

def open_nearest_number(app):
    app.stop()
    NearestNumberApp().run()

def back_games(app, webcam, clock):
    clock.stop_clock()
    webcam.release()
    open_games(app)
