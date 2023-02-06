from manim import *
from mob_default import load_mob_default
from custom_animations import GrowEachCharText
from grid import Grid
from max_sum import arr


load_mob_default(light_theme=True, square=True, background_color="#ece6e2")


class Presentacion(Scene):
    n: int = 1
    def construct(self):
        titulo = Tex(rf"\textsc{{Videos animados de\\matemáticas\\Parte {self.n}}}").scale(2).to_edge(UP)
        banner = ManimBanner(dark_theme=False)
        self.add(titulo)
        self.play(banner.create())
        self.play(banner.expand())
        que_animaciones = Text("¿Qué es Manim?", weight=BOLD).scale(1.5).to_corner(DL)
        self.play(Write(que_animaciones))
        continuar = Triangle(fill_color=BLUE, fill_opacity=1, stroke_width=0).rotate(-90 * DEGREES).to_corner(DR)
        self.play(FadeIn(continuar))


class QueEsManim(Scene):
    parrafo: str = """Manim es una herramienta para
realizar animaciones destinadas a
videos de matemáticas 2D creada
originalmente por el youtuber
3Blue1Brown. Esta imagen
también fue creada gracias a
Manim, es decir, es capaz de
crear tanto animaciones como
imágenes."""
    def construct(self):
        titulo = Tex(r"\textsc{¿Qué es Manim?}").scale(2).to_edge(UP)
        texto = Paragraph(
            *self.parrafo.split("\n"),
            t2s={"youtuber": ITALIC}
        ).to_edge(LEFT)
        self.threeb1b = SVGMobject("3b1b.svg")
        self.threeb1b_text = Text("Logo de 3Blue1Brown").scale(0.5)
        VGroup(self.threeb1b, self.threeb1b_text).arrange(DOWN).to_edge(RIGHT)
        self.seguir_leyendo = Text("Seguir leyendo", weight=BOLD).to_corner(DL)
        triangulo = Triangle(fill_color=BLUE, fill_opacity=1, stroke_width=0).rotate(-90 * DEGREES).to_corner(DR)
        self.add(titulo, texto, self.threeb1b, self.threeb1b_text, self.seguir_leyendo, triangulo)


class QueEsManim2(QueEsManim):
    parrafo: str = """Es totalmente gratuito y es capaz
de realizar animaciones muy fluidas y
requiere conocimientos de programación,
pues las animaciones de Manim se hace
con código en el lenguaje Python.
Existen muchos cursos de Manim en
internet dedicados para que profesores
interesados puedan aprender a realizar
contenido visual en la clase."""
    def construct(self):
        super().construct()
        self.remove(self.threeb1b, self.threeb1b_text)


class QueEsManim3(QueEsManim2):
    parrafo: str =  """Existen tres versiones: la de la
comunidad (la que uso actualmente),
ManimGL que hace las animaciones
mucho más rápido, y ManimCairo,
la versión más antigua, que está
disponible aún, sin embargo ya
casi no se usa debido a lo difícil
que es aprender a usarlo. Te
recomiendo que aprendas sobre Python
primero y luego que vayas con un
curso de ManimCE (la versión de la
comunidad), que es mucho más fácil
de usar. Si deseas más rapidez y
llevas experiencia, puedes usar
ManimGL."""
    def construct(self):
        super().construct()


class Animacion1(Scene):
    def construct(self):
        titulo = Tex(r"\textsc{Ejemplos de animaciones}").scale(2).to_edge(UP)
        ax = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=8, y_length=8).add_coordinates()
        labels = ax.get_axis_labels("x", "y")
        graph = ax.plot(lambda x: -1/5 * (x - 5)**2 + 5, color=RED)
        self.add(titulo)
        self.play(Write(ax))
        self.play(Write(labels), Create(graph))
        riemann = ax.get_riemann_rectangles(graph, x_range=[1, 4], dx=1)
        self.play(Write(riemann))
        for dx in [0.5, 0.25, 0.1, 0.04]:
            self.play(Transform(riemann, ax.get_riemann_rectangles(graph, x_range=[1, 4], dx=dx)), run_time=0.5)
        self.play(FadeOut(riemann))
        self.play(Write(ax.get_area(graph, x_range=[1, 4], opacity=1)))
        self.seguir_viendo = Text("Seguir viendo", weight=BOLD).to_corner(DL)
        triangulo = Triangle(fill_color=BLUE, fill_opacity=1, stroke_width=0).rotate(-90 * DEGREES).to_corner(DR)
        self.play(Write(self.seguir_viendo), FadeIn(triangulo))


class Spring(VMobject):
    def __init__(self, start=ORIGIN, length=2, bumps=14):
        self.length = length
        self.empty = 0.4
        self.step = 0.07
        self.bump = 0.18
        super().__init__(color=BLACK)
        vertices = np.array(
            [
                [0, 0, 0],
                [self.empty, 0, 0],
                [self.empty + self.step, self.bump, 0],
                *[
                    [
                        self.empty + self.step + self.step * 2 * i,
                        self.bump * (1 - (i % 2) * 2),
                        0,
                    ]
                    for i in range(1, bumps)
                ],
                [self.empty + self.step * 2 * bumps, 0, 0],
                [self.empty * 2 + self.step * 2 * bumps, 0, 0],
            ]
        )
        vertices = vertices * [self.length /
                               (1 + 0.2 * bumps), 1, 0] + np.array(start)

        self.start_new_path(np.array(start))
        self.add_points_as_corners(
            [*(np.array(vertex) for vertex in vertices)])


class Animacion2(ThreeDScene):
    def construct(self):
        titulo = Tex(r"\textsc{Ejemplos de animaciones}").scale(2).to_edge(UP)
        self.add(titulo)
        BLACK = "#343434"
        SLATE = "#a2a2a2"
        WHITE = "#ece6e2"
        W = config.frame_width
        H = config.frame_height
        ceil_len = 3
        w1 = 6
        w2 = w1 * 1.1  # w2 > w1
        # A1 = 0.2
        # A2 = 0.2
        p1 = 0
        p2 = 0
        L = 4
        l = 1.5
        sep = 2
        T = 4 * PI / (w1 + w2)
        self.renderer.background_color = WHITE
        # Setup
        a = Circle(radius=0.4, fill_opacity=1).shift(LEFT * sep + DOWN)
        b = Circle(radius=0.4, fill_opacity=1).shift(RIGHT * sep + DOWN)
        l1 = Line(a.get_center() + UP * L, a.get_center()).set_color(BLACK)
        l2 = Line(b.get_center() + UP * L, b.get_center()).set_color(BLACK)
        ceil = VGroup(
            DashedLine(
                start=ceil_len * LEFT,
                end=(ceil_len) * RIGHT,
                dashed_ratio=0.4,
                dash_length=0.2,
                color=BLACK,
            ).shift(l1.get_start()[1] * UP)
        )
        [i.rotate(PI / 4, about_point=i.get_start())
         for i in ceil[0].submobjects]
        ceil.add(
            Line(ceil_len * LEFT, ceil_len * RIGHT,
                 color=BLACK).align_to(ceil, DOWN)
        )
        spring = Spring(l1.get_start() + DOWN * l, 2 * sep)
        d1 = Dot(color=BLACK).move_to(spring.get_start())
        d2 = Dot(color=BLACK).move_to(spring.get_end())
        paint1 = Dot(color=BLACK).move_to(a.shift(DOWN))
        paint2 = Dot(color=BLACK).move_to(b.shift(DOWN))

        # Physics
        t = ValueTracker()
        A1 = ValueTracker(0.4)
        A2 = ValueTracker(0)
        l1.add_updater(
            lambda m: m.set_angle(
                A1.get_value() * np.cos(w1 * t.get_value() + p1)
                + A2.get_value() * np.cos(w2 * t.get_value() + p2)
                - PI / 2
            )
        )
        l2.add_updater(
            lambda m: m.set_angle(
                A1.get_value() * np.cos(w1 * t.get_value() + p1)
                - A2.get_value() * np.cos(w2 * t.get_value() + p2)
                - PI / 2
            )
        )
        a.add_updater(lambda m: m.move_to(l1.get_end()))
        b.add_updater(lambda m: m.move_to(l2.get_end()))

        def springupdater(m: Spring):
            # Modified Mobject.put_start_and_end_on
            curr_start, curr_end = m.get_start_and_end()
            curr_vect = curr_end - curr_start
            target_vect = (
                l2.get_start()
                + (l2.get_end() - l2.get_start()) * l / L
                - l1.get_start()
                - (l1.get_end() - l1.get_start()) * l / L
            )
            axis = (
                normalize(np.cross(curr_vect, target_vect))
                if np.linalg.norm(np.cross(curr_vect, target_vect)) != 0
                else OUT
            )
            m.stretch(
                np.linalg.norm(target_vect) / np.linalg.norm(curr_vect),
                0,
                about_point=curr_start,
            )
            m.rotate(
                angle_between_vectors(curr_vect, target_vect),
                about_point=curr_start,
                axis=axis,
            )
            m.move_to(
                l1.get_start() + (l1.get_end() - l1.get_start()) * l / L,
                aligned_edge=LEFT,
            )

        spring.add_updater(springupdater)
        d1.add_updater(lambda m: m.move_to(spring.get_start()))
        d2.add_updater(lambda m: m.move_to(spring.get_end()))

        paint1.add_updater(lambda m: m.set_x(a.get_x()))
        paint2.add_updater(lambda m: m.set_x(b.get_x()))
        trails = VGroup()

        def add_trail():
            self.play(FadeIn(paint1), FadeIn(paint2), run_time=0.4)
            trails.add(
                VGroup(
                    VMobject()
                    .start_new_path(paint1.get_center())
                    .set_stroke(color=[WHITE, BLACK])
                    .set_sheen_direction(UP),
                    VMobject()
                    .start_new_path(paint2.get_center())
                    .set_stroke(color=[WHITE, BLACK])
                    .set_sheen_direction(UP),
                )
            )
            trails[-1][0].add_updater(
                lambda m, dt: m.shift(DOWN * 0.25 * dt).add_points_as_corners(
                    [paint1.get_center()]
                )
            )
            trails[-1][1].add_updater(
                lambda m, dt: m.shift(DOWN * 0.25 * dt).add_points_as_corners(
                    [paint2.get_center()]
                )
            )

        def remove_trail(play=True):
            if play:
                self.play(FadeOut(paint1), FadeOut(paint2), run_time=0.4)
            for i in trails[-1]:
                i.clear_updaters().add_updater(
                    lambda m, dt: m.shift(
                        DOWN * 0.25 * dt
                    )  # .set_opacity(m.get_stroke_opacity() - 0.2*dt)
                )

        cfg = {"stroke_color": SLATE,
                  "stroke_width": 2, "stroke_opacity": 0.2}
        grid = NumberPlane(
            background_line_style=cfg,
            axis_config={"stroke_color": WHITE, "stroke_opacity": 0},
            x_range=(-W, W, 1.5),
            y_range=(-H / 2, H, 1.5),
        )

        rect = Rectangle(WHITE, H, W, fill_opacity=1)
        self.add(l1, l2, spring, ceil, d1,
                 d2, a, b, trails, rect, grid)
        self.play(Create(grid))
        self.play(FadeOut(rect))

        def simulate(time):
            self.play(
                t.animate.increment_value(time),
                trails[-1][0].animate.set_stroke(color=[BLACK, WHITE]),
                trails[-1][1].animate.set_stroke(color=[BLACK, WHITE]),
                rate_func=linear,
                run_time=time,
            )

        add_trail()
        simulate(10 * T)
        remove_trail()
        self.play(A1.animate.set_value(0),
                  A2.animate.set_value(0.4), run_time=2)
        add_trail()
        simulate(10 * T)
        remove_trail()
        self.play(A1.animate.set_value(0.2),
                  A2.animate.set_value(0.2), run_time=2)
        add_trail()
        simulate(25 * T)
        remove_trail(False)
        self.play(
            t.animate.increment_value(1),
            rate_func=lambda x: 2*x-x*x,
            run_time=2,
        )
        banner = ManimBanner(dark_theme=False).scale(
            0.8).move_to([0, 5, 5.5]).rotate(PI / 2, axis=RIGHT)
        banner.anim.rotate(PI / 2, axis=RIGHT)
        self.add(banner)
        self.move_camera(
            phi=PI / 2,
            theta=-PI / 2,
            frame_center=[0, 0, 5],
            added_anims=[grid.animate.set_opacity(0)],
        )
        nos_vemos = Text("Nos vemos en la parte 2", weight=BOLD).rotate(PI / 2, axis=RIGHT).next_to(banner, IN, buff=2)
        self.play(LaggedStart(banner.expand(), Write(nos_vemos)))


class Presentacion2(Presentacion):
    n: int = 2


class MessageBubble(VGroup):
    def __init__(self, message: Text | MathTex | Tex, me: bool=True):
        message.scale(0.8)
        bubble_only = RoundedRectangle(corner_radius=0.1, width=message.width + 0.2, height=message.height + 0.2)
        if me:
            bubble_only.set_fill(GREEN, opacity=1)
        else:
            bubble_only.set_fill(BLUE, opacity=1)
        super().__init__(bubble_only)
        bubble_only.set_stroke(width=0)
        if not me:
            bubble_only.flip(LEFT)
        bubble_only.scale(1.1)
        bubble_only.move_to(message)
        self.add(message)
        self.center()
        self.me = me


class Conversation(VGroup):
    def __init__(self):
        super().__init__()

    def send_message(self, message: Text | MathTex | Tex):
        message_bubble = MessageBubble(message, me=True)
        message_bubble.to_edge(RIGHT)
        if len(self) > 0:
            previous_bubble = self.get_message_by_index(-1)
            message_bubble.set_y(previous_bubble.get_y())
            message_bubble.shift((previous_bubble.height/2 + message_bubble.height/2 + 0.2) * DOWN)
        self.add(message_bubble)
        return self

    def receive_message(self, message: Text  | MathTex | Tex):
        message_bubble = MessageBubble(message, me=False)
        message_bubble.to_edge(LEFT)
        if len(self) > 0:
            previous_bubble = self.get_message_by_index(-1)
            message_bubble.set_y(previous_bubble.get_y())
            message_bubble.shift((previous_bubble.height/2 + message_bubble.height/2 + 0.2) * DOWN)
        self.add(message_bubble)
        return self
    
    def show_message_by_index(self, scene: Scene, index: int):
        message_bubble = self.get_message_by_index(index)
        if message_bubble.me:
            scene.add_sound("sending.mp3")
        else:
            scene.add_sound("receiving.mp3")
        scene.play(GrowFromCenter(message_bubble[0]))
        scene.play(GrowEachCharText(message_bubble[1]))
    
    def get_message_by_index(self, index: int) -> MessageBubble:
        return self[index]


class Animacion3(Scene):
    def construct(self):
        titulo = Tex(r"\textsc{Ejemplos de animaciones}").scale(2).to_edge(UP)
        self.add(titulo)
        activa_sonido = Tex(r"\textbf{¡Activa sonido!}").scale(2)
        self.play(GrowFromCenter(activa_sonido))
        self.wait(2)
        self.play(FadeOut(activa_sonido))

        
        partes = VGroup(
            MathTex("2", "x", "+", "7", "=", "5"),
            MathTex("2", "x", "=", "5", "-", "7"),
            MathTex("2", "x", "=", "-2"),
            MathTex("x", "=", "{-2", r"\over", "2}"),
            MathTex("x", "=", "-1")
        )
        mensajes = VGroup(
            Tex("¡Hola! Necesito ayuda porfa :("),
            Tex("Dime en qué te puedo ayudar :)"),
            VGroup(
                Tex("Es que quería resolver esta ecuación"),
                partes[0].copy()
            ).arrange(DOWN),
            Tex(r"Mira, simplemente debes despejar\\la incógnita"),
            Tex("¿Cómo podría hacer eso? :("),
            VGroup(
                partes[3],
                Tex("Mira la animación, así se hace :D")
            ).arrange(DOWN),
            Tex("Muchísimas graciaaaaas <3")
        )
        conversacion = Conversation()
        for i, mensaje in enumerate(mensajes):
            if i == 2:
                conversacion.receive_message(mensaje)
                bubble = conversacion.get_message_by_index(2)
                self.add_sound("receiving.mp3")
                self.play(GrowFromCenter(bubble[0]))
                self.play(GrowEachCharText(bubble[1][0]))
                self.play(GrowEachCharText(bubble[1][1]))
            elif i == 5:
                conversacion.send_message(mensaje)
                bubble = conversacion.get_message_by_index(5)
                eq = bubble[1][0]
                for j, parte in enumerate(partes):
                    parte.move_to(eq)
                    if j == 0:
                        self.add_sound("sending.mp3")
                        self.play(GrowFromCenter(bubble[0]))
                        self.play(GrowEachCharText(parte), GrowEachCharText(bubble[1][1]))
                    elif j == 1:
                        self.play(TransformMatchingTex(partes[0], parte, key_map={"+": "-"}))
                    elif j == 3:
                        self.play(TransformMatchingTex(partes[2], parte, key_map={"-2": "{-2", "2": "2}"}))
                    else:
                        self.play(TransformMatchingTex(partes[j - 1], parte))
            elif i == 0:
                conversacion.receive_message(mensaje)
                bubble = conversacion.get_message_by_index(0)
                bubble.next_to(titulo, DOWN, buff=2).to_edge(LEFT)
                conversacion.show_message_by_index(self, i)

            elif i in [4, 6]:
                conversacion.receive_message(mensaje)
                conversacion.show_message_by_index(self, i)
            else:
                conversacion.send_message(mensaje)
                conversacion.show_message_by_index(self, i)
        seguir_viendo = Text("Seguir viendo", weight=BOLD).to_corner(DL)
        triangulo = Triangle(fill_color=BLUE, fill_opacity=1, stroke_width=0).rotate(-90 * DEGREES).to_corner(DR)
        self.play(Write(seguir_viendo), FadeIn(triangulo))


class Animacion4(Scene):
    def construct(self):
        titulo = Tex(r"\textsc{Ejemplos de animaciones}").scale(2).to_edge(UP)
        self.add(titulo)

        code_mob = Code(
            file_name="max_sum.py",
            tab_width=4,
            background="window",
            language="Python",
            font="JetBrains Mono",
            style="monokai"
        )
        indicate_triangle = Triangle(fill_color=YELLOW, fill_opacity=1, stroke_width=0) \
            .scale(0.1).rotate(-90 * DEGREES).next_to(code_mob.line_numbers[0], LEFT)
        self.play(Write(code_mob))
        self.play(Write(indicate_triangle))
        self.play(Indicate(code_mob.code[0], scale_factor=1))
        self.play(VGroup(code_mob, indicate_triangle).animate.shift(UP))
        nombre = Text("arr", font="JetBrains Mono")
        arr_sqrs = VGroup(*[Square(side_length=1, color=BLACK).set_fill(BLUE, opacity=1) for _ in range(len(arr))]).arrange(RIGHT, buff=0)
        VGroup(nombre, arr_sqrs).arrange(DOWN).next_to(code_mob, DOWN, buff=1)
        arr_nums = VGroup(*[Integer(el).move_to(sq) for el, sq in zip(arr, arr_sqrs)])
        self.play(Write(nombre), Write(arr_sqrs), Write(arr_nums))
        self.play(indicate_triangle.animate.next_to(code_mob.line_numbers[2], LEFT))
        self.play(Indicate(code_mob.code[2], scale_factor=1))
        self.play(VGroup(code_mob, nombre, arr_sqrs, arr_nums, indicate_triangle).animate.shift(1.5 * UP))
        max_sum_name = Text("max_sum", font="JetBrains Mono")
        max_sum_sq = Square(side_length=1, color=BLACK).set_fill(BLUE, opacity=1)
        max_sum_num = Integer(0).move_to(max_sum_sq)
        max_sum_all = VGroup(max_sum_name, VGroup(max_sum_sq, max_sum_num)).arrange(DOWN).next_to(arr_sqrs, DOWN, buff=1)
        self.play(Write(max_sum_all))
        self.play(indicate_triangle.animate.next_to(code_mob.line_numbers[4], LEFT))
        self.play(Indicate(code_mob.code[4], scale_factor=1))
        for i in range(len(arr) - 4):
            arr_sum = sum(arr[i:i + 5])
            if i > 0:
                self.play(Transform(rec, SurroundingRectangle(arr_sqrs[i:i+5], color=RED, buff=0)))
            self.play(indicate_triangle.animate.next_to(code_mob.line_numbers[5], LEFT))
            self.play(Indicate(code_mob.code[5], scale_factor=1))
            if i == 0:
                rec = SurroundingRectangle(arr_sqrs[:5], color=RED, buff=0)
                self.play(Create(rec))
                self.play(VGroup(code_mob, nombre, arr_sqrs, arr_nums, indicate_triangle, max_sum_all, rec).animate.shift(UP))
                arr_sum_name = Text("arr_sum", font="JetBrains Mono")
                arr_sum_sq = Square(side_length=1, color=BLACK).set_fill(BLUE, opacity=1)
                arr_sum_num = Integer(arr_sum).move_to(arr_sum_sq)
                arr_sum_all = VGroup(arr_sum_name, VGroup(arr_sum_sq, arr_sum_num)).arrange(DOWN).next_to(max_sum_sq, DOWN, buff=1)
                self.play(Write(arr_sum_all))
            else:
                self.play(arr_sum_num.animate.set_value(arr_sum))
            self.play(indicate_triangle.animate.next_to(code_mob.line_numbers[6], LEFT))
            self.play(Indicate(code_mob.code[6], scale_factor=1))
            if arr_sum > max_sum_num.get_value():
                self.play(Indicate(VGroup(code_mob.code[6], indicate_triangle), scale_factor=1, color=GREEN))
                self.play(indicate_triangle.animate.next_to(code_mob.line_numbers[7], LEFT))
                self.play(Indicate(code_mob.code[7], scale_factor=1))
                self.play(max_sum_num.animate.set_value(arr_sum).move_to(max_sum_sq))
            else:
                self.play(Indicate(VGroup(code_mob.code[6], indicate_triangle), scale_factor=1, color=RED))
        seguir_viendo = Text("Seguir viendo", weight=BOLD).to_corner(DL)
        triangulo = Triangle(fill_color=BLUE, fill_opacity=1, stroke_width=0).rotate(-90 * DEGREES).to_corner(DR)
        self.play(Write(seguir_viendo), FadeIn(triangulo))


class Imagen1(Scene):
    def construct(self):
        titulo = Tex(r"\textsc{Ejemplos de imágenes}").scale(2).to_edge(UP)
        ax = Axes(x_range=[-2, 5, 1], y_range=[-2, 5, 1], x_length=8, y_length=8).add_coordinates()
        labels = ax.get_axis_labels("x", "y")
        graph1 = ax.plot(np.exp, x_range=[-2, np.log(5)], color=RED)
        graph2 = ax.plot(np.log, x_range=[np.exp(-2), 5], color=BLUE)
        nos_vemos = Tex(r"\textbf{Nos vemos en la parte 3}").to_edge(DOWN)
        subtitulo = MathTex(r"e^x>\ln x").scale(2).next_to(VGroup(ax, labels), UP)
        self.add(titulo, ax, labels, graph1, graph2, nos_vemos, subtitulo)


class Problema1(Scene):
    def construct(self):
        self.camera.background_color = GREY_D
        MY_YELLOW = "#ffc800"
        grid = Grid(color=MY_YELLOW, opacity=0.2)
        title = Text("Problema", weight=BOLD, font_size=96, color=WHITE).to_corner(UL)
        title_rec = BackgroundRectangle(title, color=MY_YELLOW, buff=0.4, fill_opacity=1)
        VGroup(title_rec, title).to_corner(UL, buff=0).shift(0.5 * DOWN)
        tex = MathTex(r"S_n=1!+2!+\ldots+n!", font_size=96)
        tex_rec = BackgroundRectangle(tex, color=MY_YELLOW, buff=0.4, fill_opacity=1, corner_radius=0.5)
        text = Tex(r"Encuentra todos los valores de $n$ tal que $S_n$ es un\\cuadrado perfecto", color=WHITE)
        VGroup(VGroup(tex_rec, tex), text).arrange(DOWN)
        self.add(grid, title_rec, title, tex_rec, tex, text)