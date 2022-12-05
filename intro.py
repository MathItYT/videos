from manim import *
from logo import Logo
from mob_default import load_mob_default


load_mob_default()


class Intro(Scene):
    def construct(self):
        self.play(Logo().create())
        self.wait()