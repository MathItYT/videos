from manim import NumberLine, ValueTracker, DecimalNumber, Dot, Text, VGroup, VMobject, LEFT, RIGHT, DOWN, config
from types import NoneType


class Slider(VGroup):
    def __init__(
        self,
        x_range,
        value_tracker: ValueTracker,
        length=config.frame_x_radius - 2,
        include_sign=True,
        label: VMobject | NoneType = None
    ):
        line = NumberLine(x_range, length=length)
        super().__init__(line)
        dot = Dot(line.n2p(value_tracker.get_value()), color=VMobject().color) \
            .add_updater(lambda m: m.move_to(line.n2p(value_tracker.get_value())))
        self.add(dot)
        dec = DecimalNumber(value_tracker.get_value(), group_with_commas=False, mob_class=Text, include_sign=include_sign) \
            .add_updater(lambda m: m.set_value(value_tracker.get_value()))
        dec.next_to(self[0], RIGHT)
        self.add(dec)
        if label is not None:
            label.next_to(self[0], LEFT)
            self.add(label)


class SliderGroup(VGroup):
    def __init__(self, *sliders: Slider, **kwargs):
        for mob in sliders:
            assert isinstance(mob, Slider)
        super().__init__(*sliders, **kwargs)
    
    def arrange(self):
        for m1, m2 in zip(self.submobjects[:-1], self.submobjects[1:]):
            m2[0].next_to(m1[0], DOWN)
            m2[2].next_to(m2[0], RIGHT)
            if len(m2) == 4:
                m2[3].next_to(m2[0], LEFT)
        self.center()
        return self