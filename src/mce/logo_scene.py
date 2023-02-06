# Code for ManimCE

from manim import *
from logo import LOGO_COLOR


config.background_color = LOGO_COLOR
config.frame_height = config.frame_width
config.pixel_width, config.pixel_height = 2000, 2000


class LogoScene(Scene):
    def construct(self):
        self.add(MathTex("\\sum").scale(config.frame_height / 2))


# Code for ManimGL (my personal version that you can see at https://github.com/MathLike/manimgl)

# from manimlib import *


# class LogoScene(Scene):
#     def construct(self):
#         self.add(Tex("\\sum").scale(FRAME_Y_RADIUS))