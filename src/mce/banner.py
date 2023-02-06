# Code for ManimCE

from manim import *
from logo import Logo
from mob_default import load_mob_default


config.pixel_width, config.pixel_height = 2560, 1440
config.frame_width = 2560/1440 * config.frame_height
load_mob_default()


class Banner(Scene):
    def construct(self):
        texto = VGroup(Tex("Videos cada semana con probabilidad de"), MathTex("{\\pi \\over 2}\\%"))
        texto.arrange(DOWN)
        all_g = VGroup(texto, Logo()).scale(0.7).arrange(RIGHT)
        self.add(all_g)


# Code for ManimGL (my personal version that you can see at https://github.com/MathLike/manimgl)

# from manimlib import *
# from logo import Logo


# class Banner(Scene):
#     def construct(self):
#         texto = VGroup(TexText("Videos cada semana con probabilidad de"), Tex("{\\pi \\over 2}\\%"))
#         texto.arrange(DOWN)
#         all_g = VGroup(texto, Logo()).scale(0.7).arrange(RIGHT)
#         self.add(all_g)