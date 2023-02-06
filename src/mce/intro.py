# Code for ManimCE

from manim import *
from logo import Logo
from mob_default import load_mob_default


load_mob_default()


class Intro(Scene):
    logo = Logo()

    def construct(self):
        self.play(self.logo.create())
        self.wait()


# Code for ManimGL (my personal version that you can see at https://github.com/MathLike/manimgl)

# from manimlib import *
# from logo import Logo


# class Intro(Scene):
#     def construct(self):
#         logo = Logo()
#         self.play(logo.create())
#         self.wait()