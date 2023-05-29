from kivy.lang import Builder
from kivymd.app import MDApp

import cv2 as cv
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

import imutils

class JokenpoApp(MDApp):
    def build(self):
        self.title = "Hand Games"
        self.icon = "icons/hand-games-rounded.png"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"

        self.image = Image(
            pos_hint = {'center_x': 0.5, 'y': -0.05}
        )
        layout = Builder.load_file('pages/Jokenpo/jokenpo.kv')
        layout.add_widget(self.image)

        self.capture = cv.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0/30.0)


        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        frame = imutils.resize(frame, width=500)
        self.image_frame = frame
        buffer = cv.flip(frame, -1).tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
        self.image.texture = texture