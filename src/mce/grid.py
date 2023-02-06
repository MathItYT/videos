from manim import NumberPlane


class Grid(NumberPlane):
    def __init__(self, color, opacity=1, **kwargs):
        dct = {"stroke_color": color, "stroke_opacity": opacity}
        super().__init__(background_line_style=dct, axis_config=dct, **kwargs)