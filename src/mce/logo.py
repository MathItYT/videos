# Code for ManimCE

from manim import *


LOGO_COLOR = "#2484e3"


class Logo(VMobject):
    def __init__(self, text=True):
        super().__init__()
        self.text = text
        circ = Circle(color=VMobject().color) \
            .set_fill(LOGO_COLOR, opacity=1)
        sum_symb = MathTex("\\sum", color=WHITE)
        mobs = [VGroup(circ, sum_symb)]
        if text: mobs.append(Text("MathLike", font="CMU Serif"))
        self.add(*mobs)
        if text: self.arrange(DOWN)
    
    def create(self):
        self[0].set_opacity(0)
        self[0].rotate(180 * DEGREES)
        copy = self[0].copy()
        def updater(m: VGroup, alpha):
            if alpha > 0.01:
                m.become(copy \
                    .scale(alpha) \
                    .set_opacity(alpha) \
                    .rotate(-180 * DEGREES * alpha))
                copy \
                    .scale(1 / alpha) \
                    .rotate(180 * DEGREES * alpha)
            return m
        anims = [UpdateFromAlphaFunc(self[0], updater)]
        if self.text: anims.append(Write(self[1]))
        return AnimationGroup(*anims)


# Code for ManimGL (my personal version that you can see at https://github.com/MathLike/manimgl)

# from manimlib import *


# LOGO_COLOR = "#2484e3"


# class Logo(VMobject):
#     def __init__(self, text=True):
#         super().__init__()
#         self.text = text
#         circ = Circle(stroke_color=WHITE) \
#             .set_fill(LOGO_COLOR, opacity=1)
#         sum_symb = Tex("\\sum", color=WHITE)
#         mobs = [VGroup(circ, sum_symb)]
#         if text: mobs.append(Text("MathLike"))
#         self.add(*mobs)
#         if text: self.arrange(DOWN)
    
#     def create(self):
#         self[0].set_opacity(0)
#         self[0].rotate(180 * DEGREES)
#         copy = self[0].copy()
#         def updater(m: VGroup, alpha):
#             if alpha > 0.01:
#                 m.become(copy \
#                     .scale(alpha) \
#                     .set_opacity(alpha) \
#                     .rotate(-180 * DEGREES * alpha))
#                 copy \
#                     .scale(1 / alpha) \
#                     .rotate(180 * DEGREES * alpha)
#             return m
#         anims = [UpdateFromAlphaFunc(self[0], updater)]
#         if self.text: anims.append(Write(self[1]))
#         return AnimationGroup(*anims)