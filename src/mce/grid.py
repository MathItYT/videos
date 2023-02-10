from manim import NumberPlane, VGroup, DashedLine
import numpy as np


class Grid(NumberPlane):
    def __init__(self, color, opacity=1, **kwargs):
        dct = {"stroke_color": color, "stroke_opacity": opacity}
        super().__init__(background_line_style=dct, axis_config=dct, **kwargs)


class DashedGrid(VGroup):
    def __init__(self, x_step, y_step, height=6.0, width=6.0, line_kwargs=dict(), **kwargs):
        super().__init__(**kwargs)

        for x in np.arange(-width / 2., width / 2. + x_step, x_step):
            self.add(DashedLine(
                [x, -height / 2., 0],
                [x, height / 2., 0],
                **line_kwargs
            ))
        if width % x_step != 0:
            self.remove(self[-1])
        self.center()
        x_len = len(self)
        for y in np.arange(-height / 2, height / 2 + y_step, y_step):
            self.add(DashedLine(
                [-width / 2., y, 0],
                [width / 2., y, 0],
                **line_kwargs
            ))
        if height % y_step != 0:
            self.remove(self[-1])
        self[x_len:].center()