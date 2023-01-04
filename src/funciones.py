# Code for ManimGL

from manimlib import *
from intro import Intro
from logo import Logo


class Thumbnail(Scene):
    def construct(self):
        title = Text("¿Qué es una función?").scale(2)
        subtitle = Text("Parte 1").scale(1.5)
        VGroup(title, subtitle).arrange(DOWN)
        logo = Logo().scale(0.75).to_corner(DR)
        func = Tex("y", "=", "f", "(", "x", ")") \
            .set_color_by_tex_to_color_map({"f": GREY, "x": BLUE, "y": YELLOW}) \
            .scale(2) \
            .to_corner(UL)
        self.add(title, subtitle, logo, func)


class IntroVideo(Intro):
    def construct(self):
        titulo = Text("Funciones", font_size=72).to_edge(UP)
        self.play(DrawBorderThenFill(titulo))
        subtitulo = Text("¿Qué son y para qué sirven?") \
            .next_to(titulo, DOWN)
        parte = Text("Parte 1").to_edge(DOWN)
        self.play(GrowFromEdge(subtitulo, UP))
        self.play(Write(parte))
        super().construct()
        self.play(*[FadeOut(mob) for mob in self.mobjects[1:]])


class BouncingBall(Dot):
    def __init__(self, y0=3.5, vy0 = 0, gry = 0, c=0.9, g=10, **kwargs):
        super().__init__(y0 * UP, **kwargs)
        self.v = vy0 * UP
        self.gry = gry
        self.c = c
        self.g = g
    
    def start_bouncing(self):
        self.add_updater(self.bounce_updater)
        return self

    def stop_bouncing(self):
        self.remove_updater(self.bounce_updater)
        self.v = 0 * UP
        return self

    def bounce_updater(self, m: Mobject, dt):
        dv = -self.g * dt * UP
        self.v += dv
        m.shift(self.v * dt)
        if self.get_y() <= self.gry + self.radius:
            self.v -= dv # Get back to the original velocity
            self.v *= -self.c
            m.set_y(self.gry + self.radius)


class BouncingBallScene(Scene):
    def construct(self):
        title = Text("Motivación").scale(0.75).to_corner(UL)
        self.ax = Axes(x_range=[-1, 5], y_range=[0, 5])
        labels = self.ax.get_axis_labels(r"t\text{ [s]}", r"y\text{ [m]}")
        self.play(Write(title))
        self.play(Write(VGroup(self.ax, labels)))
        self.wait()
        ball = BouncingBall(
            y0=self.ax.get_y_axis().get_top(),
            gry=self.ax.get_x_axis().get_y(),
            color=RED
        )
        ball.align_to(self.ax.get_x_axis(), LEFT)
        ball.save_state()
        self.play(ShowCreation(ball))
        ball.start_bouncing()
        self.wait(5)
        ball.stop_bouncing()
        self.wait()
        self.play(Restore(ball))
        self.wait()

        ball_copy = ball.deepcopy().set_opacity(0)
        t_tracker = ValueTracker(0)

        ball_copy.add_updater(lambda m: m.set_x(self.ax.c2p(t_tracker.get_value())[0]).set_y(ball.get_y()))
        ball.start_bouncing()
        self.path = TracedPath(ball_copy.get_center, stroke_color=YELLOW, stroke_width=4)
        self.bring_to_back(self.path, ball_copy)
        self.play(t_tracker.animate.set_value(5), run_time=5, rate_func=linear)
        ball_copy.clear_updaters()
        ball.stop_bouncing()
        self.wait()

        dot = Dot(self.ax.get_origin()).set_opacity(0)
        self.play(dot.animate.move_to(self.ax.c2p(2, 0)).set_opacity(1))
        self.wait()
        self.play(dot.animate.move_to(self.ax.i2gp(2, self.path)))
        self.wait()

        h_line = self.ax.get_h_line(dot.get_center())
        tip = ArrowTip().next_to(h_line, LEFT, buff=0)
        h_line.add(tip)
        y_coord = np.round(self.ax.p2c(dot.get_center())[1], decimals=2)
        y_coord_tex = Tex(f"{y_coord}").next_to(h_line, LEFT)
        self.bring_to_back(h_line)
        self.play(ShowCreation(h_line), Write(y_coord_tex))
        self.wait()
        self.t = ValueTracker(2)

        def dot_updater(m):
            m.move_to(self.ax.i2gp(self.t.get_value(), self.path))
        
        def h_line_updater(m):
            m.become(self.ax.get_h_line(dot.get_center()))
            tip = ArrowTip().next_to(h_line, LEFT, buff=0)
            m.add(tip)
        
        def y_coord_tex_updater(m):
            y_coord = np.round(self.ax.p2c(dot.get_center())[1], decimals=2)
            m.become(Tex(f"{y_coord}")).next_to(h_line, LEFT)

        dot.add_updater(dot_updater)
        h_line.add_updater(h_line_updater)
        y_coord_tex.add_updater(y_coord_tex_updater)
        self.play(self.t.animate.set_value(5), run_time=3)
        dot.remove_updater(dot_updater)
        h_line.remove_updater(h_line_updater)
        y_coord_tex.remove_updater(y_coord_tex_updater)
        self.wait()

        all_group = VGroup(title, ball, self.ax, labels, tip, h_line, y_coord_tex, dot, self.path)
        self.play(FadeOut(all_group))


class WhatIsFunction(Scene):
    def construct(self):
        title = Text("Concepto de función").scale(0.75).to_corner(UL)
        self.play(Write(title))
        tex_to_color_map = {
            "y": YELLOW,
            "f": GREY,
            "x": BLUE
        }
        func_tex = Tex("y", "=", "f", "(", "x", ")") \
            .set_color_by_tex_to_color_map(tex_to_color_map) \
            .scale(2)
        self.play(Write(func_tex))
        self.wait()
        f_x = func_tex[2:]
        self.play(Indicate(f_x))
        self.wait()
        self.play(Indicate(f_x[0]))
        self.play(Indicate(f_x[1:]))
        self.wait()
        self.play(Indicate(f_x))
        self.wait()
        self.play(Indicate(f_x))
        texto = TexText("$f$", " de ", "$x$") \
            .set_color_by_tex_to_color_map(tex_to_color_map) \
            .next_to(f_x, DOWN)
        self.play(GrowFromCenter(texto))
        self.wait()
        self.play(FadeOut(texto))

        g = VGroup(
            Tex("x", "=", "4"),
            Tex("y", "=", "5")
        ).arrange(RIGHT, buff=2).scale(2).next_to(func_tex, DOWN)
        for mob in g:
            mob.set_color_by_tex_to_color_map(tex_to_color_map)
            self.play(FadeIn(mob))

        self.wait()
        g_now = VGroup(
            Tex("x", "=", "3.1"),
            Tex("y", "=", "7.4")
        ).arrange(RIGHT, buff=2).scale(2).next_to(func_tex, DOWN)
        for mob in g_now: mob.set_color_by_tex_to_color_map(tex_to_color_map)
        self.play(Transform(g, g_now))
        self.wait()

        sc_rec = ScreenRectangle(height=3).to_corner(UR)
        self.play(ShowCreation(sc_rec))
        self.wait()
        self.play(Uncreate(sc_rec))
        self.wait()

        gr = VGroup(func_tex, g)
        self.play(FadeOut(gr))

        new_func = Tex("f", "(", "x", ")", "=", "2", "x", "+", "1") \
            .set_color_by_tex_to_color_map(tex_to_color_map) \
            .scale(2)
        self.play(Write(new_func))
        self.wait()

        tex_to_color_map_copy = tex_to_color_map.copy()
        tex_to_color_map_copy[r"2\relax"] = BLUE
        f_2 = Tex("f", "(", r"2\relax", ")", "=", "2", "(", r"2\relax", ")", "+", "1") \
            .set_color_by_tex_to_color_map(tex_to_color_map_copy) \
            .scale(1.5) \
            .next_to(new_func, DOWN)
        self.play(Write(f_2))
        self.wait()
        f_2_new = Tex("f", "(", r"2\relax", ")", "=", "5") \
            .set_color_by_tex_to_color_map(tex_to_color_map_copy) \
            .scale(1.5) \
            .next_to(new_func, DOWN)
        self.play(Transform(f_2, f_2_new))
        self.wait()

        self.play(FadeOut(VGroup(title, new_func, f_2)))
