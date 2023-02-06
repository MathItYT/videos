from manim import *
from logo import Logo
from intro import Intro
from custom_animations import GrowEachCharText, AddEachCharFlipping
from mob_default import load_mob_default
from sympy.abc import x
import itertools


load_mob_default()
CUSTOM_GREY = "#333333"
kw = {"font_size": 36}
arrow_label_kw = {"font_size": 24}
texs_to_color_map = {"f": GREY, "x": BLUE, "y": YELLOW}
rec_kw = {"corner_radius": 0.1, "stroke_width": 2, "buff": 0.05}


class Thumbnail(Scene):
    n: int = 2
    def construct(self):
        title = Text("¿Qué es una función?").scale(2)
        subtitle = Text(f"Parte {self.n}").scale(1.5)
        VGroup(title, subtitle).arrange(DOWN)
        logo = Logo().scale(0.75).to_corner(DR)
        func = MathTex("y", "=", "f", "(", "x", ")") \
            .set_color_by_tex_to_color_map(texs_to_color_map) \
            .scale(2) \
            .to_corner(UL)
        self.add(title, subtitle, logo, func)


class IntroVideo(Intro):
    n: int = 2
    def construct(self):
        titulo = Text("Funciones", font_size=72).to_edge(UP)
        self.play(DrawBorderThenFill(titulo))
        subtitulo = Text("¿Qué son y para qué sirven?") \
            .next_to(titulo, DOWN)
        parte = Text(f"Parte {self.n}").to_edge(DOWN)
        self.play(GrowFromEdge(subtitulo, UP))
        self.play(Write(parte))
        super().construct()
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class OnPreviousVideo(Scene):
    def construct(self):
        titulo = Text("En el video anterior").to_edge(UP)
        self.change_bg(CUSTOM_GREY)
        self.play(Write(titulo))
        
        text1 = Text("Vimos que a una función le doy un valor y me devuelve otro", **kw)
        self.play(GrowEachCharText(text1))
        self.wait()
        self.play(FadeOut(text1))
        text2 = Text("Por ejemplo:", **kw)
        self.play(GrowEachCharText(text2))
        self.play(text2.animate.next_to(titulo, DOWN))
        f_x = MathTex("f", "(", "x", ")", "=", "x^", "2") \
            .set_color_by_tex_to_color_map(texs_to_color_map) \
            .next_to(text2, DOWN)
        x = f_x[2]
        x_bottom = x.get_bottom()
        x_rec = SurroundingRectangle(x, **rec_kw)
        self.play(GrowEachCharText(f_x))
        x_arrow = Arrow(x_bottom, x_bottom + DOWN)
        self.play(Create(x_arrow), Create(x_rec))
        text3 = Text("Un número desconocido", **arrow_label_kw).next_to(x_arrow, DOWN)
        self.play(Write(text3))
        self.wait()
        text4 = Text("Puede tomar cualquier valor", **arrow_label_kw).next_to(x_arrow, DOWN)
        self.play(ReplacementTransform(text3, text4))
        self.wait()
        y = f_x[5:]
        y_bottom = y.get_bottom()
        y_rec = SurroundingRectangle(y, **rec_kw)
        y_arrow = Arrow(y_bottom, y_bottom + DOWN)
        self.play(FadeOut(text4), ReplacementTransform(VGroup(x_rec, x_arrow), VGroup(y_rec, y_arrow)))
        text5 = Text("El mismo número al cuadrado", **arrow_label_kw) \
            .next_to(y_arrow, DOWN)
        self.play(Write(text5))
        self.wait()
        text6 = Tex(
            r"O sea, cualquier número\\que le de a la función ",
            r"$f\relax$\\",
            r"siempre me lo elevará al cuadrado",
            **arrow_label_kw
        ).set_color_by_tex(r"f\relax", GREY).next_to(y_arrow, DOWN)
        self.play(ReplacementTransform(text5, text6))
        self.wait(3)

        self.play(FadeOut(y_arrow, text6), Uncreate(y_rec))
        ejemplo = MathTex("f", "(", "3", ")", "=", "9") \
            .set_color_by_tex_to_color_map({"f": GREY, "3": BLUE, "9": YELLOW}) \
            .next_to(f_x, DOWN, buff=1)
        self.play(GrowEachCharText(ejemplo))
        self.wait()
        explicacion = Tex(
            "Porque a ", r"$f\relax$", " le metí ", "$3$", " y ", "$3^2=9$",
            **kw
        ).set_color_by_tex_to_color_map({r"f\relax": GREY}).next_to(ejemplo, DOWN)
        explicacion[3].set_color(BLUE)
        explicacion[5][0].set_color(BLUE)
        explicacion[5][-1].set_color(YELLOW)
        self.play(GrowEachCharText(explicacion))
        self.wait(2)
        self.play(FadeOut(titulo, text2, f_x, ejemplo, explicacion))
        self.change_bg(BLACK)
     
    def change_bg(self, target_color):
        old_color = self.camera.background_color

        def bg_updater(m, alpha):
            self.camera.background_color = interpolate_color(old_color, target_color, alpha)
            return m

        self.play(UpdateFromAlphaFunc(Mobject(), bg_updater))


class IntroVideo(Intro):
    def construct(self):
        super().construct()
        self.play(ShrinkToCenter(self.logo))


class QueEsProductoCartesiano(Scene):
    def construct(self):
        titulo = Text("¿Qué es el producto cartesiano?").to_edge(UP)
        self.play(AddEachCharFlipping(titulo))
        self.wait()
        definicion_natural = Tex("Tenemos dos conjuntos: ", "$A$", " y ", "$B$") \
            .set_color_by_tex_to_color_map({"A": BLUE, "B": YELLOW})
        self.play(Write(definicion_natural))
        self.wait()
        self.play(definicion_natural.animate.next_to(titulo, DOWN))
        a_elements = []
        b_elements = []
        lst1 = [1, 2, 3]
        lst2 = ["x", "y"]
        for i, x in enumerate(lst1):
            to_sum = [str(x)]
            if i != len(lst1) - 1:
                to_sum.append(",")
            a_elements += to_sum
        for i, x in enumerate(lst2):
            to_sum = [x]
            if i != len(lst2) - 1:
                to_sum.append(",")
            b_elements += to_sum
        a = MathTex("A", "=", r"\{", *a_elements, r"\}")
        b = MathTex("B", "=", r"\{", *b_elements, r"\}")
        set_tex_map = {"A": BLUE, "B": YELLOW}
        for set_ in [a, b]:
            set_.set_color_by_tex_to_color_map(set_tex_map)
            set_[3:-1:2].set_color(GREY)
        sets = VGroup(a, b).arrange(DOWN)
        self.play(Write(sets))
        self.wait()
        text1 = Tex(
            r"""Por supuesto existe un conjunto con todos\\
            los pares ordenados que resultan de poner\\
            primero un elemento de """, "$A$ ", r"""y luego un\\
            elemento de """, "$B$", font_size=24
        ).set_color_by_tex_to_color_map(set_tex_map) \
            .to_edge(DOWN).shift(0.5 * UP)
        self.play(Write(text1))
        self.wait(3)
        def element_to_mobject(e):
            result = MathTex(e, substrings_to_isolate=[*a_elements, *b_elements])
            result[1::2].set_color(GREY)
            return result
        top_left_entry = VGroup(Line(DL / 2, UR / 2))
        top_left_entry.add(MathTex("A", color=BLUE), MathTex("B", color=YELLOW))
        top_left_entry[1].shift(0.25 * UL)
        top_left_entry[2].shift(0.2 * DR)
        top_left_entry.scale(0.7)
        table_elems = [[f"({a_el},{b_el})" for b_el in b_elements[::2]] for a_el in a_elements[::2]]
        table = MathTable(
            table_elems,
            col_labels=[MathTex(b_el, color=GREY) for b_el in b_elements[::2]],
            row_labels=[MathTex(a_el, color=GREY) for a_el in a_elements[::2]],
            element_to_mobject=element_to_mobject,
            top_left_entry=top_left_entry,
            v_buff=0.2,
            h_buff=0.2
        )
        self.play(ReplacementTransform(VGroup(a, b), table))
        self.wait()
        text2 = Text("Con esta tabla pudimos obtener el conjunto que quisimos", font_size=36).next_to(table, DOWN, buff=1)
        self.play(ReplacementTransform(text1, text2))
        self.wait()

        the_set_elems = []
        for part in table_elems:
            the_set_elems += part
        for i, part in enumerate(the_set_elems):
            if i < len(the_set_elems) - 1:
                the_set_elems[i] = part + ","
        the_set = MathTex("C", "=", r"\{", *the_set_elems, r"\}", substrings_to_isolate=[*a_elements, *b_elements], font_size=36) \
            .set_color_by_tex_to_color_map({elem: GREY for elem in a_elements + b_elements}) \
            .next_to(text2, DOWN)
        the_set[0].set_color(GREEN)
        self.play(GrowEachCharText(the_set))
        self.wait()
        text3 = Tex(
            r"""Un conjunto que se obtenga de todos los\\
            pares posibles con primera parte un elemento de\\""",
            "$A$", " y segunda parte un elemento de ", r"$B$\\",
            "será el producto cartesiano entre ", "$A$", " y ", "$B$",
            font_size=24
        ) \
            .set_color_by_tex_to_color_map(set_tex_map) \
            .next_to(table, DOWN, buff=1)
        self.play(the_set.animate.next_to(definicion_natural, DOWN))
        self.play(ReplacementTransform(text2, text3))
        self.wait(3)

        the_set_elems = {**set_tex_map, "C": GREEN}
        text4 = Tex("¡Entonces ", "$C$", r" es el producto cartesiano\\", "entre ", "$A$", " y ", "$B$", "!", font_size=36) \
            .set_color_by_tex_to_color_map(the_set_elems) \
            .next_to(table, DOWN, buff=1)
        self.play(ReplacementTransform(text3, text4))
        self.wait()
        c_equals = MathTex("C", "=", "A", r"\times", "B", font_size=36) \
            .set_color_by_tex_to_color_map(the_set_elems) \
            .next_to(text4, DOWN)
        self.play(Write(c_equals))
        self.play(Circumscribe(c_equals))
        self.wait()

        the_set_elems = {**the_set_elems, r"a\relax": GREY, "b": GREY}
        definicion_matematica = MathTex(
            "A", r"\times", "B", "=", r"\{", "(", r"a\relax", ",", "b", ")", ":", r"a\relax", r"\in", "A",
            r"\land", "b", r"\in", "B", r"\}"
        ) \
            .set_color_by_tex_to_color_map(the_set_elems)
        self.play(FadeOut(table))
        self.play(AddEachCharFlipping(definicion_matematica))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))