from manim import *


class GrowEachCharText(LaggedStart):
    def __init__(self, mobject: Mobject, **kwargs):
        animations = self.extract_animations(mobject)
        super().__init__(*animations, **kwargs)
    
    def extract_animations(self, mobject: Mobject):
        result = []
        if len(mobject.submobjects) > 0:
            for submobject in mobject.submobjects:
                result += self.extract_animations(submobject)
        else:
            result.append(GrowFromCenter(mobject))
        return result


class ShrinkEachCharText(LaggedStart):
    def __init__(self, mobject: Mobject, fade_out=False, **kwargs):
        animations = self.extract_animations(mobject, fade_out)
        super().__init__(*animations, **kwargs)

    def extract_animations(self, mobject: Mobject, fade_out):
        result = []
        if len(mobject.submobjects) > 0:
            for submobject in mobject.submobjects:
                result += self.extract_animations(submobject, fade_out)
        else:
            if fade_out is False:
                anim = ShrinkToCenter(mobject)
            else:
                anim = FadeOut(mobject, scale=0.5)
            result.append(anim)
        return result


class CreateFlipping(Animation):
    def __init__(self, mobject: Mobject, **kwargs):
        assert isinstance(mobject, Mobject)
        super().__init__(mobject, **kwargs)
    
    def interpolate_mobject(self, alpha: float) -> None:
        self.mobject.become(self.starting_mobject)
        self.mobject.rotate(270 * DEGREES + 90 * DEGREES * alpha, axis=UP)


class AddEachCharFlipping(LaggedStart):
    def __init__(self, mobject: Text | MathTex | Tex, **kwargs):
        assert isinstance(mobject, (Text, MathTex, Tex))
        if isinstance(mobject, Text):
            animations = [CreateFlipping(char) for char in mobject]
        else:
            animations = [CreateFlipping(char) for part in mobject for char in part]
        super().__init__(*animations, **kwargs)


class GrowAndShrinkABit(Animation):
    def interpolate_mobject(self, alpha: float) -> None:
        self.mobject.become(self.starting_mobject)
        self.mobject.scale(-2.4 * alpha**2 + 3.4 * alpha)


class GrowAndShrinkABitEachChar(LaggedStart):
    def __init__(self, mobject, **kwargs):
        animations = self.extract_animations(mobject)
        super().__init__(*animations, **kwargs)

    def extract_animations(self, mobject: Mobject):
        result = []
        if len(mobject.submobjects) > 0:
            for submobject in mobject.submobjects:
                result += self.extract_animations(submobject)
        else:
            result.append(GrowAndShrinkABit(mobject))
        return result


class FadeInFromLeft(LaggedStart):
    def __init__(self, mobject: Mobject, **kwargs):
        animations = self.extract_animations(mobject)
        super().__init__(*animations, **kwargs)
    
    def extract_animations(self, mobject: Mobject):
        result = []
        if len(mobject.submobjects) > 0:
            for submobject in mobject.submobjects:
                result += self.extract_animations(submobject)
        else:
            result.append(FadeIn(mobject, shift=RIGHT))
        return result