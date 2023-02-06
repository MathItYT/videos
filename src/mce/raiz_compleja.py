from manim import *
from voiceover import VoiceoverScene # Different from Manim Voiceover plugin, see voiceover.py
from scene_composition import VoiceoverComposition
from custom_animations import GrowEachCharText, ShrinkEachCharText
from logo import Logo
from intro import Intro
from blocks import DefinitionBlock
from mob_default import load_mob_default


load_mob_default()


a_cross_b_block = DefinitionBlock(
    VGroup(
        Tex(r"El producto cartesiano entre $A$ y $B$, $A\times B$, se\\ define como", color=BLACK, tex_environment=None),
        MathTex(
            "A", r"\times", "B", "=", r"\{", "(", r"a\relax", ",", "b", ")", ":",
            r"a\relax", r"\in", "A", r"\land", "b", r"\in", "B", r"\}", color=BLACK
        )
    ).arrange(DOWN),
    index=1
)


class Thumbnail(Scene):
    def construct(self):
        titulo = Text("Raíz cuadrada compleja", font_size=90).to_edge(UP)
        raiz_compleja = MathTex(r"\sqrt{", "z}", "=", r"\sqrt{", "r}", r"e^{", "i", r"\theta", r"\over", "2}").scale(4)
        raiz_compleja.set_color_by_gradient(BLUE, GREEN)
        logo = Logo().scale(0.75).to_corner(DR)
        self.add(titulo, raiz_compleja, logo)


class Introduccion(VoiceoverScene):
    def construct(self):
        with self.voiceover("Aquí tenemos la función raíz cuadrada principal real"):
            f_tex_to_color_map = {"f": GREY, "x": BLUE, r"\mathbb{R}^+_0": YELLOW}
            f = MathTex("f", ":", r"\mathbb{R}^+_0", r"\to", r"\mathbb{R}^+_0") \
                .set_color_by_tex_to_color_map(f_tex_to_color_map)
            f_x = MathTex("f", "(", "x", ")", "=", "\sqrt{", "x}") \
                .set_color_by_tex_to_color_map(f_tex_to_color_map)
            VGroup(f, f_x).arrange(DOWN)
            self.play(GrowEachCharText(f))
            self.play(GrowEachCharText(f_x))
        
        with self.voiceover(
            """A esta función le puedo dar cualquier número positivo o cero y me
            devuelve otro número positivo o cero"""
        ):
            self.play(VGroup(f, f_x).animate.to_edge(UP))
            sqrt = MathTex("f", "(", "9", ")", "=", "3") \
                .set_color_by_tex_to_color_map({"f": GREY, "9": BLUE, "3": YELLOW})
            self.play(GrowEachCharText(sqrt))
        
        with self.voiceover("También está este ejemplo"):
            sqrt_ = MathTex("f", "(", "25", ")", "=", "5") \
                .set_color_by_tex_to_color_map({"f": GREY, "5": YELLOW, "25": BLUE})
            self.play(Transform(sqrt, sqrt_))


class Introduccion2(VoiceoverScene):
    def construct(self):
        with self.voiceover(
            """Pero lamentablemente no existe número real que cumpla ser raíz cuadrada
            de un número negativo"""
        ):
            sqrt_minus_1 = MathTex("f", "(", "-1", ")") \
                .set_color_by_tex_to_color_map({"f": GREY, "-1": BLUE})
            self.play(GrowEachCharText(sqrt_minus_1))
            cross = Cross(sqrt_minus_1)
            self.play(Create(cross))
        
        with self.voiceover(
            """Aunque sí podemos hacerlo en otro conjunto que incluye a los números reales,
            aparte de otros números"""
        ):
            self.play(FadeOut(sqrt_minus_1, cross))
            c = MathTex(r"\mathbb{C}").scale(3)
            self.play(GrowFromCenter(c))
            def updater(m, alpha):
                m.set_color(interpolate_color(WHITE, YELLOW_D, alpha))
            self.play(UpdateFromAlphaFunc(c, updater, rate_func=there_and_back, run_time=3))
        
        with self.voiceover("La raíz cuadrada de un número negativo existe en los números complejos"):
            numeros_complejos = Text("Números complejos").next_to(c, DOWN)
            c_group = VGroup(c, numeros_complejos)
            self.play(Write(numeros_complejos))
            self.play(c_group.animate.center())
        
        with self.voiceover(
            """Este conjunto es un cuerpo, es decir, cumple 5 propiedades fundamentales
            en la suma y producto, además de la propiedad distributiva. Si deseas
            que demuestre esto, pídelo en los comentarios"""
        ):
            self.play(c_group.animate.scale(2/5).to_edge(UP))
            def propiedad(string):
                return f"{string} en $+$ y $\\cdot$"
            strings = ["Cerradura", "Asociatividad", "Conmutatividad", "Elemento neutro", "Elemento opuesto"]
            lst = BulletedList(
                *[propiedad(string) for string in strings],
                r"Distributividad de $\cdot$ respecto a $+$"
            )
            self.play(GrowEachCharText(lst))
        
        with self.voiceover("En este video aprenderás sobre la raíz cuadrada compleja. Ahora sí comencemos"):
            self.play(ShrinkToCenter(VGroup(c_group, lst)))
            suscribete = Text("SUSCRÍBETE", color=RED).scale(2)
            self.play(GrowEachCharText(suscribete))
            self.wait(2)
            self.play(ShrinkEachCharText(suscribete))


class IntroduccionComposition(VoiceoverComposition, Intro):
    scenes = [Introduccion, Introduccion2, Intro]


class ContenidoDelVideo(Scene):
    i: int = 0
    def construct(self):
        titulo = Text("Contenido del video").to_edge(UP)
        table = MobjectTable([
            [Tex("Conceptos previos"), BulletedList("Producto cartesiano", "Relaciones", "Funciones")],
            [Tex("Raíz cuadrada real"), BulletedList("Raíces cuadradas de un número", "Raíz cuadrada principal")],
            [Tex("Números complejos"), BulletedList("Para qué", "Propiedades", "Forma polar")],
            [Tex("Raíz cuadrada compleja"), BulletedList("")]
        ])
        self.play(GrowEachCharText(titulo))
        self.play(Write(lst))


class ProductoCartesiano(VoiceoverScene):
    def construct(self):
        with self.voiceover("Primero vamos a partir resumiendo conceptos previos, como el producto cartesiano"):
            titulo = Text("¿Qué es el producto cartesiano?").to_edge(UP)
            self.play(GrowEachCharText(titulo))
        
        with self.voiceover("Tenemos dos conjuntos, A y B"):
            self.play(titulo.animate.to_edge(UP))
            set1 = MathTex("A", "=", r"\{", "X", ",", "X", ",", "X", r"\}") \
                .set_color_by_tex("A", BLUE)
            to_replace = set1[3:8:2]
            dots = VGroup(*[Dot(color=dot_color) for dot_color in (PURE_RED, WHITE, PURE_BLUE)])
            for i, dot, replaced in zip(range(3, 8, 2), dots, to_replace):
                dot.replace(replaced)
                set1.submobjects[i] = dot
            set2 = MathTex("B", "=", r"\{", "1", ",", "2", ",", "3", ",", "4", r"\}") \
                .set_color_by_tex("B", YELLOW)
            VGroup(set1, set2).arrange(DOWN)
            self.play(GrowEachCharText(set1))
            self.play(GrowEachCharText(set2))
        
        with self.voiceover(
            """Para que se entienda la idea del producto cartesiano, diremos que el par ordenado
            pelotita roja con número 2 pertenece al producto cartesiano entre A y B"""
        ):
            red_ball = dots[0].copy()
            tex_to_color_map = {"A": BLUE, "B": YELLOW}
            belongs = MathTex("(", "X", ",", "2", ")", r"\in", "A", r"\times", "B") \
                .set_color_by_tex_to_color_map(tex_to_color_map).to_edge(DOWN)
            red_ball.replace(belongs[1])
            belongs.submobjects[1] = red_ball
            self.play(GrowEachCharText(belongs))
            self.wait(2)
            self.play(ShowPassingFlash(Underline(belongs, color=YELLOW)))
        
        with self.voiceover("Debido a que la primera componente es un elemento de A y la segunda de B"):
            belongs_a = MathTex("X", r"\in", "A").set_color_by_tex_to_color_map(tex_to_color_map)
            red_ball_2 = red_ball.copy()
            red_ball_2.replace(belongs_a[0])
            belongs_a.submobjects[0] = red_ball_2
            belongs_b = MathTex("2", r"\in", "B").set_color_by_tex_to_color_map(tex_to_color_map)
            belongs_g = VGroup(belongs_a, belongs_b).arrange(DOWN).to_edge(DOWN)
            self.play(belongs.animate.next_to(belongs_g, UP))
            self.play(GrowEachCharText(belongs_a))
            self.play(GrowEachCharText(belongs_b))
        
        with self.voiceover("Lo mismo aplica para pelota azul con 3"):
            blue_ball = dots[2].copy()
            blue_ball.replace(belongs_a[0])
            blue_ball_copy = blue_ball.copy()
            blue_ball_copy.replace(belongs[1])
            three = MathTex("3")
            three_copy = three.copy()
            three.replace(belongs_b[0])
            three_copy.replace(belongs[3])
            def func(g):
                g[0].submobjects[0] = blue_ball
                g[1].submobjects[0] = three
                g[2].submobjects[1], g[2].submobjects[3] = blue_ball_copy, three_copy
                return g
            self.play(ApplyFunction(func, VGroup(belongs_a, belongs_b, belongs)))
        
        with self.voiceover(
            """Pero eso no se da en el orden inverso, porque tiene que estar
            en el orden elemento de A coma elemento de B, no al revés"""
        ):
            def func(m):
                m.become(MathTex("(", "3", ",", "X", ")", r"\in", "A", r"\times", "B") \
                    .set_color_by_tex_to_color_map(tex_to_color_map).move_to(m))
                three_copy.replace(m[1]), blue_ball_copy.replace(m[3])
                m.submobjects[1], m.submobjects[3] = three_copy, blue_ball_copy
                return m
            self.play(ApplyFunction(func, belongs))
            cross = Cross(belongs)
            self.play(Create(cross))
        
        with self.voiceover(
            """O sea el producto cartesiano entre A y B sería el resultado
            de poner todas las combinaciones entre elementos de A primero y
            elementos de B segundo, dicho en lenguaje matemático como se
            muestra en pantalla"""
        ):
            self.play(FadeOut(set1, set2, belongs, belongs_a, belongs_b), Uncreate(cross))
            self.play(a_cross_b_block.create())