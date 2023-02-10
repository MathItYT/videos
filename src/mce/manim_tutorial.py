from manim import *
from custom_animations import GrowAndShrinkABitEachChar, ShrinkEachCharText
from scene_composition import VoiceoverComposition
from intro import Intro
from logo import Logo
from enumerated_list import EnumeratedList
from grid import DashedGrid
from slider import Slider
from slider import SliderGroup
from mob_default import load_mob_default


load_mob_default(light_theme=True, background_color="#ece6e2")


class Trailer(Scene):
    logo = Logo()
    def construct(self):
        Intro.construct(self)
        self.remove(*self.mobjects)
        pronto = Text("Pronto")
        self.play(Write(pronto))
        self.wait()
        self.play(FadeOut(pronto))
        nuevo_curso = Tex("Curso de ", "MM", " en español", font_size=72)
        m_banner = ManimBanner(dark_theme=False).replace(nuevo_curso[1])
        nuevo_curso.submobjects[1] = m_banner
        self.play(GrowAndShrinkABitEachChar(nuevo_curso[::2]), m_banner.create())
        buff1 = m_banner.get_left()[0] - nuevo_curso[0].get_right()[0]
        buff2 = nuevo_curso[2].get_left()[0] - m_banner.get_right()[0]
        y1 = nuevo_curso[0].get_y()
        y2 = nuevo_curso[2].get_y()
        def updater1(m): return m.next_to(m_banner, LEFT, buff=buff1).set_y(y1)
        def updater2(m): return m.next_to(m_banner, RIGHT, buff=buff2).set_y(y2)
        self.play(
            UpdateFromFunc(nuevo_curso[0], updater1),
            UpdateFromFunc(nuevo_curso[2], updater2),
            m_banner.expand()
        )
        self.wait()
        self.play(FadeOut(nuevo_curso[0], nuevo_curso[2]), m_banner.animate.scale(2))
        self.wait()
        python = ImageMobject("python.png").scale_to_fit_height(m_banner.height)
        plus = MathTex("+").scale(2)
        self.play(FadeIn(python), Write(plus), Group(python, plus, m_banner).animate.arrange(RIGHT, buff=0.5))
        aprende = Text("¡Aprende a crear videos animados de matemáticas!", font_size=36).to_edge(DOWN)
        self.play(GrowAndShrinkABitEachChar(aprende))
        self.wait()
        self.play(FadeOut(*self.mobjects))


class Contenido(Scene):
    def construct(self):
        abp = Text("Aprendizaje basado en proyectos")
        self.play(GrowAndShrinkABitEachChar(abp))
        self.wait()
        self.play(ShrinkEachCharText(abp, fade_out=True))
        lst = EnumeratedList(
            "Demostración algebraica: desigualdad AM-GM",
            "Comportamiento de una sinosuide",
            "Algoritmo de ordenamiento",
            r"Simulación de física con ayuda de \texttt{pymunk}",
            r"Demostración visual: $\displaystyle\lim_{x\to 0}{\sin x \over x}=1$",
            "¡Y mucho más!"
        )
        self.play(Write(lst))
        self.wait()
        lst_copy = lst.copy()
        scene_classes = [DemoAlg, ComportamientoSinusoide, BlankScene, BlankScene, BlankScene, BlankScene]
        for i, scene_class in enumerate(scene_classes):
            run_time = 1 if i in (0, 1) else 0.25
            if i == 0:
                for part in lst_copy:
                    part.to_corner(UL)
                self.play(FadeOut(lst[1:]), ReplacementTransform(lst[0], lst_copy[0]))
            else:
                self.play(Write(lst_copy[i]), run_time=run_time)
            scene_class.construct(self)
            if len(self.mobjects) > 0:
                self.play(FadeOut(*self.mobjects))


class DemoAlg(Scene):
    def construct(self):
        enunciado1 = Tex("Demuestra el siguiente enunciado:")
        enunciado2 = MathTex(
            r"\forall",
            "a",
            ",",
            "b",
            r"\in",
            r"\mathbb{R}^+_0",
            r"\bigg(",
            "{a",
            "+",
            "b",
            r"\over",
            "2}",
            r"\geq",
            r"\sqrt{",
            "a",
            "b}",
            r"\bigg)"
        )
        enunciado = VGroup(enunciado1, enunciado2).arrange(DOWN)
        self.play(GrowAndShrinkABitEachChar(enunciado))
        self.wait()
        self.play(ShrinkEachCharText(enunciado))
        sabemos1 = Tex(r"Sabemos que para todo $x\in\mathbb{R}$")
        sabemos2 = MathTex("x", "^2", r"\geq", "0")
        sabemos = VGroup(sabemos1, sabemos2).arrange(DOWN)
        self.play(FadeIn(sabemos, shift=RIGHT))
        self.wait()
        digamos = MathTex("x", "=", "a", "-", "b").to_edge(DOWN)
        digamos_ = MathTex("a", "-", "b").replace(digamos[2:])
        nota = Tex("Sustitución").next_to(digamos, UP)
        self.play(GrowFromCenter(digamos))
        self.play(Indicate(digamos, color=BLACK))
        self.play(FadeIn(nota))
        self.wait()
        sabemos_2 = MathTex("(", "a", "-", "b", ")", "^2", r"\geq", "0").move_to(sabemos2)
        self.play(TransformMatchingTex(VGroup(digamos_, sabemos2), sabemos_2))
        self.play(FadeOut(nota, digamos, shift=DOWN), FadeOut(sabemos1))
        self.play(sabemos_2.animate.center())
        self.wait()
        br = Brace(sabemos_2[:6], DOWN)
        tex = br.get_tex(
            r"a\relax",
            r"^2\relax",
            "-",
            "2",
            "a",
            "b",
            "+",
            r"b\relax",
            r"^2\relax"
        )
        self.play(Write(VGroup(br, tex)))
        self.wait()
        sabemos_3 = MathTex(
            r"a\relax",
            r"^2\relax",
            "-",
            "2",
            "a",
            "b",
            "+",
            r"b\relax",
            r"^2\relax",
            r"\geq",
            "0"
        )
        self.play(TransformMatchingTex(VGroup(tex, sabemos_2), sabemos_3), Unwrite(br))
        self.wait()
        sumar1 = Tex("Suma a ambos lados")
        sumar2 = MathTex("4", r"a\relax", r"b\relax")
        sumar = VGroup(sumar1, sumar2).arrange(DOWN).to_edge(DOWN)
        self.play(FadeIn(sumar, shift=UP))
        self.wait()
        sabemos_4 = MathTex(
            r"a\relax",
            r"^2\relax",
            r"+\relax",
            "2",
            "a",
            "b",
            "+",
            r"b\relax",
            r"^2\relax",
            r"\geq",
            "4",
            r"a\relax\relax",
            r"b\relax\relax"
        )
        self.play(TransformMatchingTex(sabemos_3, sabemos_4, transform_mismatches=True, key_map={"-": r"+\relax"}))
        br2 = Brace(sabemos_4[:9], DOWN)
        tex2 = br2.get_tex("(", "a", r"+\relax", "b", ")", "^2")
        sabemos_5 = MathTex(
            "(",
            "a",
            r"+\relax",
            "b",
            ")",
            "^2",
            r"\geq",
            "4",
            r"a\relax\relax",
            r"b\relax\relax"
        )
        self.wait()
        self.play(FadeOut(sumar))
        self.play(Write(VGroup(br2, tex2)))
        self.wait()
        self.play(TransformMatchingTex(VGroup(tex2, sabemos_4), sabemos_5), Unwrite(br2))
        self.wait()
        arrows = VGroup(*[Arrow(mob.get_bottom(), mob.get_bottom() + DOWN) for mob in sabemos_5[-3:]])
        plus = VGroup(*[MathTex("+", font_size=24).next_to(arrow, DOWN) for arrow in arrows])
        self.play(Create(arrows))
        self.play(Write(plus))
        cdots = VGroup(*[
            MathTex(r"\cdot", font_size=24).move_to((plus[i].get_right() + plus[i + 1].get_left()) / 2)
            for i in range(len(plus) - 1)
        ])
        self.play(Write(cdots))
        br3 = Brace(plus, DOWN)
        tex3 = br3.get_tex("+")
        self.play(Write(VGroup(br3, tex3)))
        self.wait()
        sabemos_6 = MathTex(
            "(",
            "a",
            r"+\relax",
            "b",
            ")",
            "^2",
            r"\geq",
            "4",
            r"a\relax\relax",
            r"b\relax\relax",
            r"\geq\relax",
            "0"
        )
        self.play(FadeOut(arrows, plus, cdots, br3, tex3), TransformMatchingTex(sabemos_5, sabemos_6))
        nota2_1 = Tex("Nótese que para cualquier $x$ e $y$")
        nota2_2 = MathTex(r"x\geq y\geq 0\Rightarrow\sqrt{x}\geq\sqrt{y}").to_edge(DOWN)
        nota2 = VGroup(nota2_1, nota2_2).arrange(DOWN).to_edge(DOWN)
        self.play(FadeIn(nota2, shift=UP))
        self.play(Indicate(nota2, color=BLACK))
        self.wait()
        sabemos_7 = MathTex(
            r"\sqrt{\relax"
            "(",
            "a",
            r"+\relax",
            "b",
            ")",
            "^2}",
            r"\geq",
            r"\sqrt{",
            "4",
            r"a\relax\relax",
            r"b\relax\relax}"
        )
        self.play(
            FadeOut(nota2),
            TransformMatchingTex(
                sabemos_6, sabemos_7,
                key_map={"^2": "^2}", r"b\relax\relax": r"b\relax\relax}"}
            )
        )
        self.wait()
        sabemos_8 = MathTex(
            "|",
            "a",
            r"+\relax",
            "b",
            "|",
            r"\geq",
            "2",
            r"\sqrt{",
            r"a\relax\relax",
            r"b\relax\relax}"
        )
        self.play(TransformMatchingTex(sabemos_7, sabemos_8, transform_mismatches=True))
        self.wait()
        br4 = Brace(sabemos_8[1:4])
        tex4 = br4.get_tex(r"\geq", "0")
        self.play(Write(VGroup(br4, tex4)))
        nota3 = MathTex(r"x\geq 0\Rightarrow |x|=x").to_edge(DOWN)
        self.play(GrowFromCenter(nota3))
        self.wait()
        sabemos_9 = MathTex(
            "a",
            r"+\relax",
            "b",
            r"\geq",
            "2",
            r"\sqrt{",
            r"a\relax\relax",
            r"b\relax\relax}"
        )
        self.play(TransformMatchingTex(sabemos_8, sabemos_9), Unwrite(VGroup(br4, tex4)))
        self.play(ShrinkToCenter(nota3))
        final = MathTex(
            "{a",
            r"+\relax",
            "b",
            r"\over",
            "2}",
            r"\geq",
            r"\sqrt{",
            r"a\relax\relax",
            r"b\relax\relax}"
        )
        self.play(TransformMatchingTex(sabemos_9, final, key_map={"a": "{a"}))
        self.play(Circumscribe(final))
        self.wait()


class InterfazSinusoidal(VGroup):
    def __init__(self, a, k, omega, phi, t, **kwargs):
        self.a = a
        self.k = k
        self.omega = omega
        self.phi = phi
        self.t = t
        width = config.frame_width - 1
        height = 3
        grid = DashedGrid(
            x_step=1/2, y_step=1/2, width=width, height=height,
            line_kwargs={"color": GREY_B, "stroke_opacity": 0.5, "stroke_width": 2}
        )
        rec1 = SurroundingRectangle(grid, color=BLACK, fill_opacity=1, buff=0, stroke_width=0, corner_radius=0.5)
        rec2 = SurroundingRectangle(rec1, color=GREY_B, fill_opacity=1, buff=0.5, stroke_width=0)
        self.ax = Axes(
            x_range=[-width / 2, width/2, 1/2],
            y_range=[-3, 3, 1],
            x_length=width,
            y_length=height,
            axis_config={"stroke_color": GREY_B, "stroke_width": 4},
            tips=False
        )
        graph = always_redraw(lambda: self.ax.plot(lambda x: self.func(x), color=RED))
        super().__init__(rec2, rec1, grid, self.ax, graph, **kwargs)

    def func(self, x):
        return self.a.get_value() * np.sin(self.k.get_value() * x
                        + self.omega.get_value() * self.t.get_value()
                        + self.phi.get_value())


class ComportamientoSinusoide(Scene):
    def construct(self):
        a = ValueTracker(1)
        k = ValueTracker(1)
        omega = ValueTracker(1)
        phi = ValueTracker(0)
        t = ValueTracker(0)
        self.add(a, k, omega, phi, t)
        interfaz = InterfazSinusoidal(a, k, omega, phi, t).to_edge(DOWN)
        self.play(Write(interfaz))
        expr = MathTex(r"y(x,t)=A\sin(kx+\omega t+\phi)")
        time = MathTex("t=", "0.00")
        t_dec = DecimalNumber(0.0, group_with_commas=False, mob_class=Text).replace(time[1])
        t_dec.add_updater(lambda m: m.set_value(t.get_value()))
        time.submobjects[1] = t_dec
        expr_g = VGroup(expr, time).arrange(DOWN).to_corner(UR).shift(DOWN)
        x_range = [-3, 3, 1]
        sliders = SliderGroup(
            Slider(x_range, a, length=config.frame_x_radius / 2, label=MathTex("A")),
            Slider(x_range, k, length=config.frame_x_radius / 2, label=MathTex("k")),
            Slider(x_range, omega, length=config.frame_x_radius / 2, label=MathTex(r"\omega")),
            Slider(x_range, phi, length=config.frame_x_radius / 2, label=MathTex(r"\phi"))
        ).arrange().scale(0.5).next_to(interfaz, UP).to_edge(LEFT)
        self.play(Write(sliders), Write(expr_g))
        self.wait()
        self.play(a.animate.set_value(3), rate_func=there_and_back, run_time=3)
        self.play(a.animate.set_value(-3), rate_func=there_and_back, run_time=3)
        self.play(k.animate.set_value(-3), rate_func=there_and_back, run_time=3)
        self.play(k.animate.set_value(3), rate_func=there_and_back, run_time=3)
        self.play(phi.animate.set_value(-3), rate_func=there_and_back, run_time=3)
        self.play(phi.animate.set_value(3), rate_func=there_and_back, run_time=3)
        t.add_updater(lambda m, dt: m.increment_value(dt))
        self.wait()
        self.play(omega.animate.set_value(3), rate_func=there_and_back, run_time=3)
        self.play(omega.animate.set_value(-3), run_time=1.5)
        self.wait(2)


class BlankScene(Scene):
    def construct(self):
        self.wait()


class Outro(Scene):
    def construct(self):
        text = Text("Curso de ManimCE").to_edge(UP)
        banner = ManimBanner(dark_theme=False)
        text2 = Text("Pronto").to_edge(DOWN)
        self.play(Write(text))
        self.play(banner.create())
        self.play(GrowFromCenter(text2))


class Video(VoiceoverComposition):
    logo = Logo()
    scenes = [Trailer, Contenido, Outro]
    music_files = [("music.mp3", 0)]


class Proyecto1(VoiceoverComposition):
    def construct(self):
        with self.voiceover(
            """Hola gente, bienvenidos al primer tutorial de Manim
            Community Edition. El curso entero está diseñado de una
            manera distinta, pues acá en vez de pasar los temas por
            tópicos, vamos a ir viendo proyectos como el de este
            tutorial que están viendo ahora. Este curso incluye
            desafíos, desafíos que tú mismo tendrás que subir
            completados a YouTube, recuerda etiquetarme con @mathlike.
            También fomentaré la comprensión lectora en el sentido que
            para algunos de estos desafíos te pondré un enlace a la
            documentación. También deberás crear tus propias
            animaciones, animaciones que no están incluidas en Manim,
            pero que tú mismo puede crear, también crear objetos, etc.
            Sin más preámbulos, comencemos."""
        ):
            DemoAlg.construct(self)