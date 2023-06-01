from time import time
from typing import List

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from cv2 import VideoCapture, flip
from imutils import resize
from numpy import ndarray
from handtracking import HandDetector
from handtracking.utils import detect_skin, statistical_mode

from games import nearestNumber

global lbl_timer

class NearestNumberApp(MDApp):
    def build(self):
        self.title: str = "Hand Games"
        self.icon: str = "icons/hand-games-rounded.png"
        self.theme_cls.theme_style: str = "Light"
        self.theme_cls.primary_palette: str = "Gray"
        self.start_game_flag: bool = False
        self.fps_flag: bool = True
        self.timer_duration: int = 3
        self.amount_fingers: List[int] = []
        self.hand_detector: HandDetector = HandDetector(max_num_hands=4)
        self.fps_start_time: float = 0
        self.image = Image(
            pos_hint = {'center_x': 0.5, 'y': -0.05}
        )

        layout = Builder.load_file('pages/NearestNumber/nearestNumber.kv')
        layout.add_widget(self.image)

        self.capture = VideoCapture(0)
        self.clock = Clock
        self.clock.schedule_interval(self.load_video, 1.0/30.0)


        return layout

    def load_video(self, *args):
        success, frame = self.capture.read()

        if(success):
            image_to_process: ndarray = detect_skin(frame)
            frame = resize(frame, width=500)

            self.hand_detector.process_image(image_to_process)
            image_with_landmarks = self.hand_detector.draw_landmarks(frame)
            number_fingers: int = self.hand_detector.number_fingers()

            fps_end_time: float = time()
            fps: float = 1/(fps_end_time - self.fps_start_time)
            self.fps_start_time: float = fps_end_time

            current: float = time()

            if(self.start_game_flag):
                elapsed_time = current - self.start_timer
                time_left = self.timer_duration - elapsed_time

                self.amount_fingers.append(number_fingers)

                if(time_left <= 0):
                    self.start_game_flag = False
                    print(f"Dedos: {self.amount_fingers}")
                    print(f"Moda dedos: {statistical_mode(self.amount_fingers)}")
                    
                    if(evenOdd.is_even(statistical_mode(self.amount_fingers))):
                        self.root.ids.lbl_winner.text = "O jogador que escolheu PAR venceu!"
                    else:
                        self.root.ids.lbl_winner.text = "O jogador que escolheu ÍMPAR venceu!"
                    
                    self.amount_fingers.clear()

                    self.root.ids.lbl_timer.text = ""
                else:
                    self.root.ids.lbl_timer.text = f"Iniciando em: {int(time_left)}s"

            buffer = flip(image_with_landmarks, -1).tostring()
            
            texture = Texture.create(
                size = (
                    image_with_landmarks.shape[1], 
                    image_with_landmarks.shape[0]
                ), 
                colorfmt='bgr'
            )

            texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
            self.image.texture = texture

            if(self.fps_flag):
                self.root.ids.lbl_fps.text = f"FPS: {int(fps)}"

    def start_game(self) -> None:
        self.root.ids.lbl_winner.text = ""
        self.start_game_flag = True
        self.start_timer: float = time()