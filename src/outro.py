# Code for ManimCE

# from manim import *
# from mob_default import load_mob_default


# load_mob_default()


# class Outro(Scene):
#     def construct(self):
#         self.camera.background_color = "#333333"
#         suscribete = Text("¡Suscríbete!", font_size=72).to_edge(UP)
#         gracias = Text("¡Gracias por ver!", color=YELLOW).to_edge(DOWN)
#         self.play(Write(suscribete), GrowFromCenter(gracias), run_time=1)
#         self.play(Indicate(suscribete), run_time=1)
#         self.wait(18)

from manimlib import *


class Outro(Scene):
    def construct(self):
        suscribete = Text("¡Suscríbete!", font_size=72).to_edge(UP)
        gracias = Text("¡Gracias por ver!", color=YELLOW).to_edge(DOWN)
        self.play(Write(suscribete), GrowFromCenter(gracias), run_time=1)
        self.play(Indicate(suscribete), run_time=1)
        self.wait(18)