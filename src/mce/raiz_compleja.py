from manim import *
from voiceover import VoiceoverScene # Different from Manim Voiceover plugin, see voiceover.py
from scene_composition import VoiceoverComposition
from custom_animations import GrowEachCharText, ShrinkEachCharText
from logo import Logo
from intro import Intro
from mob_default import load_mob_default


load_mob_default()


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


class FormulaEulerIntro(VoiceoverScene):
    def construct(self):
        formula_euler = Text("Fórmula de Euler")
        with self.voiceover("Fórmula de Euler"):
            self.play(GrowEachCharText(formula_euler))
        self.play(ShrinkEachCharText(formula_euler))


class FormulaEuler1(VoiceoverScene):
    def construct(self):
        with self.voiceover(
            """Los números complejos en su forma binómica son a + bi,
            con a y b números reales"""
        ):
            tex_to_color_map = {"z": GREY, "a": BLUE, r"b\relax": YELLOW, r"\mathbb{R}": GREY, r"i\relax": GREY}
            z_tex = MathTex("z", "=", "a", "+", r"b\relax", r"i\relax") \
                .set_color_by_tex_to_color_map(tex_to_color_map)
            rec = BackgroundRectangle(z_tex, BLACK, buff=0.2, corner_radius=0.1)
            self.add(rec)
            rec.add_updater(lambda m: m.move_to(z_tex))
            self.play(Write(z_tex))
            self.wait()
            a_b_in_R = MathTex("a", ",", r"b\relax", r"\in", r"\mathbb{R}") \
                .set_color_by_tex_to_color_map(tex_to_color_map) \
                .next_to(z_tex, DOWN)
            self.play(GrowEachCharText(a_b_in_R))
        
        with self.voiceover("Si graficas un número complejo en el denominado plano complejo, resultará esto"):
            z = ComplexValueTracker(2 + 1j)
            ax = Axes().add_coordinates()
            labels = ax.get_axis_labels(r"\Re", r"\Im")
            dot = Dot(ax.c2p(z.get_value().real, z.get_value().imag), color=GREY)
            self.play(
                Write(VGroup(ax, labels)),
                Create(dot),
                FadeOut(a_b_in_R),
                z_tex.animate.next_to(dot, RIGHT, aligned_edge=DOWN)
            )
            self.bring_to_front(rec, z_tex)
        
        with self.voiceover("En el punto, la abscisa será la parte real y la ordenada la parte imaginaria"):
            dot.add_updater(lambda m: m.move_to(ax.c2p(z.get_value().real, z.get_value().imag)))
            z_tex.add_updater(lambda m: m.next_to(dot, RIGHT, aligned_edge=DOWN))
            self.play(z.animate.set_value(-3 - 2j))
            self.wait(2)
            a_b_vals = VGroup(
                MathTex("a", "=", "-3"),
                MathTex("b", "=", "-2")
            ).arrange(DOWN).to_corner(DR)
            for mob in a_b_vals:
                mob: MathTex
                mob.set_color_by_tex_to_color_map({"a": BLUE, "b": YELLOW, "-": GREY})
            self.play(GrowEachCharText(a_b_vals))