from manim.mobject.text.tex_mobject import Tex, MathTex
from manim.constants import MED_LARGE_BUFF, LEFT, MED_SMALL_BUFF, DOWN


class EnumeratedList(Tex):
    def __init__(
        self,
        *items,
        start=1,
        buff=MED_LARGE_BUFF,
        number_scale_factor=1,
        tex_environment=None,
        **kwargs,
    ):
        self.buff = buff
        self.number_scale_factor = number_scale_factor
        self.tex_environment = tex_environment
        line_separated_items = [s + "\\\\" for s in items]
        super().__init__(
            *line_separated_items, tex_environment=tex_environment, **kwargs
        )
        for i, part in enumerate(self, start=start):
            dot = MathTex(f"{i}.").scale(self.number_scale_factor)
            dot.next_to(part[0], LEFT, MED_SMALL_BUFF)
            part.add_to_back(dot)
        self.arrange(DOWN, aligned_edge=LEFT, buff=self.buff)

    def fade_all_but(self, index_or_string, opacity=0.5):
        arg = index_or_string
        if isinstance(arg, str):
            part = self.get_part_by_tex(arg)
        elif isinstance(arg, int):
            part = self.submobjects[arg]
        else:
            raise TypeError(f"Expected int or string, got {arg}")
        for other_part in self.submobjects:
            if other_part is part:
                other_part.set_fill(opacity=1)
            else:
                other_part.set_fill(opacity=opacity)