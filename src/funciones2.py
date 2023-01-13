from manimlib import *
from funciones import Thumbnail, IntroVideo


class Thumbnail2(Thumbnail):
    n: int = 2


class IntroVideo2(IntroVideo):
    n: int = 2


class OnPreviousVideo(Scene):
    def construct(self) -> None:
        self.update_bg("#333333")
        title = Text("En el video anterior", font_size=72).to_edge(UP)
        rec = ScreenRectangle()
        self.play(Write(title))
        self.play(ShowCreation(rec))
        self.wait()
        self.play(FadeOut(title), Uncreate(rec))
        self.update_bg(BLACK)

    def update_bg(self, target_color):
        old_color = rgba_to_color(self.camera.background_rgba)
        
        def updater(m, alpha):
            color = interpolate_color(old_color, target_color, alpha)
            self.camera.background_rgba = list(color_to_rgba(color))
            return m
        
        self.play(UpdateFromAlphaFunc(Mobject(), updater))



class Example(Scene):
    def construct(self) -> None:
        pass