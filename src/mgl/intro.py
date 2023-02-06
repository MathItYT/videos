from manimlib import *
from mgl.logo import Logo


class Intro(Scene):
    def construct(self):
        logo = Logo()
        self.play(logo.create())
        self.wait()