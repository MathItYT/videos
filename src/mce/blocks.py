from manim.mobject.geometry.polygram import RoundedRectangle
from manim.mobject.geometry.shape_matchers import SurroundingRectangle
from manim.mobject.types.vectorized_mobject import VGroup
from manim.mobject.text.text_mobject import Text
from manim.mobject.text.tex_mobject import MathTex
from manim.mobject.mobject import Mobject
from manim.constants import UL, UR, RIGHT, LEFT, BOLD
from manim.utils.color import BLUE, BLUE_E
from manim.animation.composition import Succession
from manim.animation.creation import DrawBorderThenFill
from manim._config import config
from custom_animations import GrowEachCharText


class Block(VGroup):
    def __init__(
        self,
        mobject: Mobject,
        label: str,
        index: int,
        fill_color,
        stroke_color,
        width: float = config.frame_width - 3,
        **kwargs
    ):
        label = Text(label, font_size=36, weight=BOLD, color=stroke_color, disable_ligatures=True)
        index = Text(str(index), font_size=36, weight=BOLD, color=stroke_color)
        rec = RoundedRectangle(height=mobject.height + 1, width=width, color=stroke_color, corner_radius=0.2, **kwargs)
        mobject.next_to(rec.get_left(), RIGHT, buff=0.5)
        self.center_mathtex(mobject)
        rec.set_fill(fill_color, opacity=1)
        label_g = VGroup(SurroundingRectangle(label, stroke_color, corner_radius=0.1), label).move_to(rec.get_corner(UL), aligned_edge=LEFT)
        index_g = VGroup(SurroundingRectangle(index, stroke_color, corner_radius=0.1), index).move_to(rec.get_corner(UR), aligned_edge=RIGHT)
        label_g.shift(RIGHT)
        index_g.shift(LEFT)
        label_g[0].set_fill(fill_color, opacity=1), index_g[0].set_fill(fill_color, opacity=1)
        super().__init__(rec, label_g, index_g, mobject)
        self.center()
    
    def create(self):
        return Succession(
            DrawBorderThenFill(self[0]),
            DrawBorderThenFill(VGroup(self[1][0], self[2][0])),
            GrowEachCharText(VGroup(self[1][1], self[2][1])),
            GrowEachCharText(self[3])
        )
    
    def center_mathtex(self, mobject: Mobject):
        if type(mobject) == MathTex:
            mobject.set_x(0)
        elif len(mobject.submobjects) == 0:
            return
        else:
            for submobject in mobject.submobjects:
                self.center_mathtex(submobject)


class DefinitionBlock(Block):
    def __init__(self, mobject: Mobject, index: int, **kwargs):
        super().__init__(mobject, "Definición", index, BLUE, BLUE_E, **kwargs)