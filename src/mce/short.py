from manim import *
from intro import Intro
from custom_animations import GrowEachCharText, ShrinkEachCharText
from mob_default import load_mob_default
from logo import Logo
from voiceover import VoiceoverScene


load_mob_default(light_theme=True, shorts=True, background_color="#ece6e2")


class IntroVideo(Intro):
    logo = Logo().scale(2)


class Iniciando(VoiceoverScene, MovingCameraScene):
    def construct(self):
        self.record_audio("Tenemos una sucesión recursiva")
        matematicas = Text("Matemáticas").scale(2)
        self.play(GrowEachCharText(matematicas, run_time=1))
        self.play(ShrinkEachCharText(matematicas, run_time=1))
        self.wait_until_finished()
        self.record_audio("x sub n + 1 igual a 1 más 1 sobre x sub n")
        sucesion = MathTex("x_{n+1}", "=", "1", "+", "{1", r"\over", "x_n}") \
            .scale(2) 
        self.play(GrowEachCharText(sucesion))
        self.wait_until_finished()
        self.record_audio("Con x sub 0 igual a 1, o sea que parte en 1")
        x_0 = MathTex("x_0", "=", "1").scale(2)
        self.play(sucesion.animate.shift(UP))
        x_0.next_to(sucesion, DOWN)
        self.play(Write(x_0))
        self.wait_until_finished()
        self.record_audio("Calculamos el siguiente término, que es x sub 1")
        self.play(VGroup(sucesion, x_0).animate.to_edge(UP))
        x_1 = MathTex("x_1", "=", "1", "+", "{1", r"\over", "x_0}") \
            .scale(2) \
            .next_to(x_0, DOWN)
        self.play(Write(x_1))
        self.wait_until_finished()
        self.record_audio("x sub 0 es 1, así que x sub 1 es lo que se ve en pantalla")
        new_x_1 = MathTex("x_1", "=", "1", "+", "{1", r"\over", "1}") \
            .scale(2) \
            .next_to(x_0, DOWN)
        self.play(Transform(x_1, new_x_1))
        self.wait_until_finished()
        self.record_audio("Que da como resultado 2")
        new_x_1 = MathTex("x_1", "=", "2") \
            .scale(2) \
            .next_to(x_0, DOWN)
        self.play(Transform(x_1, new_x_1))
        self.wait_until_finished()
        now = 2
        tex = x_1
        self.record_audio("Bueno. Si seguimos haciendo esto una y otra vez, la sucesión convergerá a un valor específico como podemos ver en la animación")
        for i in range(2, 21):
            new_x_tex = MathTex(f"x_{{{i}}}", "=", "1", "+", "{1", r"\over", "{0}}}".format(now)) \
                .scale(2) \
                .next_to(tex, DOWN)
            self.play(TransformMatchingTex(tex.copy(), new_x_tex), run_time=0.2)
            now = 1 + 1 / now
            new_new_x_tex = MathTex(f"x_{{{i}}}", "=", f"{now}") \
                .scale(2) \
                .next_to(tex, DOWN)
            self.play(Transform(new_x_tex, new_new_x_tex), run_time=0.2)
            tex = new_x_tex
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(tex).shift(config.frame_width / 2 * UP + DOWN))
        self.play(Restore(self.camera.frame))


class Iniciando2(VoiceoverScene):
    def construct(self):
        self.record_audio("Lo que estoy haciendo es aproximar al número phi aplicando sucesiones recursivas")
        x = 1
        for _ in range(20):
            x = 1 + 1/x
        tex = MathTex("{1", "+", r"\sqrt{", "5}", r"\over", "2}", r"\approx", f"{x}").scale(2)
        self.play(GrowEachCharText(tex))
        self.wait_until_finished()
        self.record_audio(
            """La razón áurea valdría aproximadamente el término en n igual a 20 de la sucesión,
aunque en realidad una mejor aproximación se obtendría con un valor mucho más grande,
y siempre la aproximación será mejor con un n más grande que el que tuvieramos en un
momento"""
        )
        x_20 = MathTex("x_{20}").scale(2)
        arrow = Arrow(ORIGIN, 2 * DOWN).next_to(tex[-1], DOWN)
        x_20.next_to(arrow, DOWN)
        self.play(Create(arrow))
        self.play(Write(x_20))
        self.wait(2)
        text = Tex(r"Mientras mayor sea $n$, más cercano a $\varphi$ será $x_n$").next_to(tex, DOWN, buff=3)
        self.play(GrowEachCharText(text))
        self.wait(5)
        self.play(ShrinkEachCharText(text))
        self.wait_until_finished()
        self.record_audio("O sea, el límite de la sucesión es el número de oro")
        lim = MathTex(r"\lim_{", "n", r"\to", r"\infty}", "x_n", "=", r"\varphi").scale(2)
        self.play(ShrinkEachCharText(tex), Uncreate(arrow), Unwrite(x_20))
        self.play(GrowEachCharText(lim))
        self.wait_until_finished()


class Geometricamente(VoiceoverScene):
    def construct(self):
        grid = NumberPlane()
        self.record_audio("Ahora si nosotros vemos esto gráficamente, sería bastante bonito")
        self.play(Write(grid))
        graph1 = grid.plot(lambda x: 1 + 1/x, x_range=[1 / (config.frame_y_radius - 1), config.frame_x_radius], color=RED)
        graph2 = grid.plot(lambda x: 1 + 1/x, x_range=[-config.frame_x_radius, 1 / (-config.frame_y_radius - 1)], color=RED).reverse_points()
        graph3 = grid.plot(lambda x: x, color=GREEN)
        self.play(Create(graph2), Create(graph1))
        self.play(Create(graph3))
        self.wait_until_finished()

        self.record_audio("Acá tenemos las gráficas de la función identidad, la cual es g(x)=x y además f(x)=1+1/x")
        graph12_tex = MathTex("f", "(", "x", ")", "=", "1", "+", "{1", r"\over", "x}")
        graph3_tex = MathTex("g", "(", "x", ")", "=", "x")
        graph12_g = VGroup(Line(ORIGIN, RIGHT / 2, color=RED), graph12_tex).arrange(RIGHT)
        graph3_g = VGroup(Line(ORIGIN, RIGHT / 2, color=GREEN), graph3_tex).arrange(RIGHT)
        g = VGroup(graph12_g, graph3_g)
        graph3_g.next_to(graph12_g, DOWN, aligned_edge=DL)
        g.to_corner(RIGHT).to_edge(DOWN, buff=2)
        rec = SurroundingRectangle(g, color=BLACK).set_fill(GREY, opacity=1)
        self.play(Create(rec), Write(g))
        self.wait_until_finished()

        x_g = VGroup()
        x_n = 1

        for i in range(21):
            bool_ = i == 0
            bool2 = i == 1
            bool3 = i == 2
            run_time = 1 if i < 3 else 0.2
            if i == 3:
                self.record_audio(
                    """Si vamos repitiendo el proceso muchas veces, vamos viendo que el punto converge a esa intersección entre f y g,
                    que como estamos viendo el comportamiento de la sucesión gráficamente, tendría algo que ver con el límite,
                    ¿no es cierto?"""
                )
                phi = (1 + np.sqrt(5)) / 2
                self.play(FocusOn(grid.c2p(phi, phi)))
            if bool_:
                self.record_audio("Tenemos que el x inicial era 1")
            elif bool2:
                self.record_audio("x1 sería 1 + 1/x0, que justamente es f(x0)")
                dot = Dot(grid.c2p(1, 0))
                path = TracedPath(dot.get_center)
                self.play(Create(dot))
                self.add(path)
            elif bool3:
                self.record_audio("Tú te preguntas de seguro para qué lo movimos a la gráfica de la función identidad")
                self.wait_until_finished()
                self.record_audio("Y es que x2 será 1 + 1/x1, o sea f(x1). ¡Y ahora es sólo cosa de proyectar verticalmente este punto en la gráfica de f!")
            val = x_n if bool_ else 1 + 1/x_n
            x_n_tex = MathTex(f"x_{{{i}}}", "=", f"{np.round(val, decimals=2)}")
            if bool_:
                x_n_tex.to_corner(UL)
            else:
                x_n_tex.next_to(x_g[-1], DOWN).to_edge(LEFT)
            x_g.add(x_n_tex)
            x_copy = x_g.copy()
            if bool_:
                new_rec = SurroundingRectangle(x_copy, color=BLACK).set_fill(GREY, opacity=1)
            if bool_ or bool2 or bool3:
                self.wait_until_finished()
            if bool2:
                self.record_audio("El punto negro que puse ahora está justamente en (x0, 0), o sea en (1, 0)")
                self.play(FocusOn(dot))
                self.wait_until_finished()
                self.record_audio("Como dije, x1 es igual a f(x0)")
                self.wait_until_finished()
                self.record_audio(
                    """Es decir, si proyectamos verticalmente el punto en la gráfica de f, obtendríamos el punto
                    (x0, f(x0)), o sea (x0, x1)"""
                )
            if i > 0:
                self.play(dot.animate.move_to(grid.c2p(x_n, 1 + 1/x_n)), run_time=run_time)
                x_n = 1 + 1/x_n
            if bool2:
                self.wait_until_finished()
            if bool2:
                self.record_audio(
                    "Ahora este punto lo moveremos a (x1, g(x1)), que al ser la función identidad, será (x1, x1)"
                )
            elif bool3:
                self.record_audio("Ahora de nuevo lo moveremos a la función identidad y repetiremos el proceso todo el tiempo")
            if i > 0:
                self.play(dot.animate.move_to(grid.c2p(x_n, x_n)), run_time=run_time)
            if bool2:
                self.wait_until_finished()
            if bool_:
                self.play(Create(new_rec), GrowEachCharText(x_g[-1]))
            else:
                x_g[:-1].set_z_index(2)
                new_new_rec = SurroundingRectangle(x_copy, color=BLACK).set_fill(GREY, opacity=1)
                self.play(Transform(new_rec, new_new_rec), GrowEachCharText(x_g[-1]), run_time=run_time)
            if i == 20 or bool3:
                self.wait_until_finished()
        
        self.play(Uncreate(new_rec), Unwrite(x_g))
        self.record_audio("Sé que se ven puros 1,62, pero eso es porque estamos redondeando a dos cifras decimales. Como ustedes saben, el punto se acerca a una intersección entre f y g, o sea, el límite de la sucesión, llamémosle x, va a cumplir f(x)=g(x)")
        eqs_g = VGroup()
        eq = MathTex("f", "(", "x", ")", "=", "g", "(", r"x\relax", ")").to_corner(UL)
        eqs_g.add(eq)
        rec = SurroundingRectangle(eqs_g, color=BLACK).set_fill(GREY, opacity=1)
        self.play(Create(rec), Write(eq))
        self.wait_until_finished()
        self.record_audio("O sea, esto de acá. Para obtener el límite, o sea x, basta con resolver la ecuación")
        eq2 = MathTex("x", "=", "1", "+", "{1", r"\over", "x}").next_to(eq, DOWN)
        eqs_g.add(eq2)
        eqs_g[:-1].set_z_index(2)
        self.play(Transform(rec, SurroundingRectangle(eqs_g, color=BLACK).set_fill(GREY, opacity=1)), TransformMatchingTex(eq.copy(), eq2, key_map={r"x\relax": "x}"}))
        self.wait_until_finished()
        self.record_audio("Tenemos un x en el denominador y como no podemos aceptar un 0 en un denominador, x jamás será 0")
        self.wait_until_finished()
        self.record_audio("Teniendo eso en cuenta, multiplicamos por x la ecuación y obtendremos una ecuación cuadrática")
        eq3 = MathTex("x", "^2", "=", "x", "+", "1").next_to(eq2, DOWN)
        eqs_g.add(eq3)
        eqs_g[:-1].set_z_index(2)
        self.play(Transform(rec, SurroundingRectangle(eqs_g, color=BLACK).set_fill(GREY, opacity=1)), TransformMatchingTex(eq2.copy(), eq3, key_map={"{1": "1"}))
        eq4 = MathTex("x", "^2", "-", "x", "-", "1", "=", "0").next_to(eq3, DOWN)
        eqs_g.add(eq4)
        eqs_g[:-1].set_z_index(2)
        self.play(Transform(rec, SurroundingRectangle(eqs_g, color=BLACK).set_fill(GREY, opacity=1)), TransformMatchingTex(eq3.copy(), eq4, transform_mismatches=True))
        self.wait_until_finished()
        self.record_audio("Y sabemos que una de las soluciones de la ecuación es este número, ¡que es phi!")
        eq5 = MathTex("x", "=", "{1", "+", r"\sqrt{", "5}", r"\over", "2}").next_to(eq4, DOWN)
        eqs_g.add(eq5)
        eqs_g[:-1].set_z_index(2)
        self.play(Transform(rec, SurroundingRectangle(eqs_g, color=BLACK).set_fill(GREY, opacity=1)), Write(eq5))
        self.wait_until_finished()
        self.record_audio("Ahora va una pregunta: si iniciamos la sucesión con cualquier otro número real distinto de 1 y de 0 por supuesto, ¿también llegaremos a tener el mismo número?")
        self.play(Uncreate(dot), Uncreate(path))
        self.wait_until_finished()
        self.record_audio("Porque si empezamos con x0=-3, miren lo que tenemos")
        new_dot = Dot(grid.c2p(-3, 0))
        new_path = TracedPath(new_dot.get_center)
        self.play(Create(new_dot))
        self.add(new_path)
        
        x_n = -3
        for _ in range(21):
            self.play(new_dot.animate.move_to(grid.c2p(x_n, 1 + 1/x_n)), run_time=0.2)
            x_n = 1 + 1/x_n
            self.play(new_dot.animate.move_to(grid.c2p(x_n, x_n)), run_time=0.2)

        self.wait_until_finished()


class Video1(VoiceoverScene, MovingCameraScene):
    logo = Logo().scale(2)
    def construct(self):
        scene_classes = [IntroVideo, Iniciando, Iniciando2, Geometricamente]
        for i, scene in enumerate(scene_classes):
            scene.construct(self)
            if len(self.mobjects) > 0 and i < len(scene_classes) - 1:
                self.remove(*self.mobjects)
        self.add_music()


class QueEsUnLimite(VoiceoverScene, MovingCameraScene):
    def construct(self):
        self.record_audio("Primero que todo, debemos entender qué es un límite, el qué significa que un número sea el límite de una sucesión")
        lim = MathTex(r"\lim_{", "n", r"\to", r"\infty}", "x_n", "=", "l").scale(2)
        self.play(GrowEachCharText(lim))
        self.wait_until_finished()
        self.record_audio("Para ello, vamos a una gráfica")
        self.play(lim.animate.to_edge(UP))
        grid = NumberPlane(x_range=[-config.frame_x_radius, 100, 1]).add_coordinates(font_size=48)
        grid.to_edge(LEFT, buff=0)
        self.bring_to_back(grid)
        self.play(Write(grid))
        self.wait_until_finished()
        self.record_audio(
            """Este es un conjunto discreto de puntos. El eje horizontal es el n que indica si es el término inicial,
o el segundo, tercero, etc. El eje vertical representa justamente el valor del término en ese n."""
        )
        def func(n):
            return 11/2**n + 1
        dots = VGroup(*[Dot(grid.c2p(n, func(n)), color=RED) for n in range(100)])
        self.play(GrowEachCharText(dots, run_time=5))
        coord = MathTex("(", "n", ",", "x_n", ")").next_to(dots[2], UP, aligned_edge=RIGHT)
        self.play(Write(coord))
        self.wait_until_finished()
        self.record_audio("El límite de una sucesión es en términos simples el valor al que se acerca la sucesión al hacer nuestro n cada vez más grande")
        frame = self.camera.frame
        frame.save_state()
        self.play(Unwrite(coord))
        self.play(frame.animate.shift(85 * RIGHT))
        line = DashedLine(grid.c2p(-config.frame_x_radius, 1), grid.c2p(100, 1))
        self.play(Create(line), run_time=3)
        self.wait_until_finished()
        self.record_audio("Está bastante claro que la sucesión se acerca cada vez más a 1, entonces el límite de esta sucesión en particular es 1")
        self.play(Restore(frame), run_time=3)
        self.wait_until_finished()