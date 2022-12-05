from manim import *
from logo import LOGO_COLOR


config.background_color = LOGO_COLOR
config.frame_height = config.frame_width
config.pixel_width, config.pixel_height = 2000, 2000


class LogoScene(Scene):
    def construct(self):
        self.add(MathTex("\\sum").scale(config.frame_height / 2))