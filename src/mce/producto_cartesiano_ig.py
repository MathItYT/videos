from manim import *
from logo import Logo
from mob_default import load_mob_default

if sys.argv[1] == "producto_cartesiano_ig.py":
    load_mob_default(
        light_theme=True, background_color=WHITE, square=True, text_font="Poppins", vmob_default_color="#1f284f",
        custom_font_tex="Poppins"
    )


MATH_GREEN = "#178a32"


class ProductoCartesiano1(Scene):
    def construct(self):
        logo = Logo().to_corner(UR)
        titulo = Text("Producto\ncartesiano", font_size=144)
        subtitulo = Text("¿Qué es?", font_size=96)
        titulo.set_color_by_gradient(GREEN, BLUE)
        subtitulo.set_color_by_gradient(GREEN, BLUE)
        VGroup(titulo, subtitulo).arrange(DOWN).next_to(logo, DOWN).set_x(0)
        producto = MathTex(r"A\times B").scale(4).to_edge(DOWN, buff=3)
        guardado = ImageMobject("guardado_ig.png").scale_to_fit_height(1).to_corner(DR)
        botones = Group(
            ImageMobject("like_ig.png"),
            ImageMobject("comentario_ig.png"),
            ImageMobject("enviar_ig.png")
        )
        for boton in botones: boton.scale_to_fit_height(1)
        botones.arrange(RIGHT).to_corner(DL)
        self.add(titulo, subtitulo, producto, botones, guardado, logo)


class ProductoCartesiano2(Scene):
    def construct(self):
        text = Tex(
            r"""Es muy importante saber qué es el\\
            producto cartesiano si vas a estudiar\\
            el concepto de relaciones en\\
            profundidad. Para explicar este\\
            concepto, voy a recurrir a un ejemplo:\\
            Tenemos dos conjuntos, """,
            "$A$", " y ", "$B$", ".",
            font_size=54, tex_environment=None
        ).set_color_by_tex("$", MATH_GREEN)
        a = MathTex(r"A=\{a,b,c\}", color=MATH_GREEN, font_size=54)
        b = MathTex(r"B=\{1,2,3,4\}", color=MATH_GREEN, font_size=54)
        text2 = Tex(
            r"""Si sacamos un par ordenado que\\
            tenga un elemento de """, "$A$", r" y un\\elemento de ",
            "$B$", r" en el orden\\mencionado, por ejemplo, ",
            "$(a,3)$", r",\\diremos que éste pertenece a ",
            r"$A\times B$", r".\\Lo mismo aplica para ", "$(c,1)$",
            r". Sin\\embargo, no aplicará para, por",
            font_size=54, tex_environment=None
        ).set_color_by_tex("$", MATH_GREEN)
        contenido = VGroup(text, a, b, text2).arrange(DOWN, aligned_edge=LEFT)
        for mob in (a, b):
            mob.set_x(0)
        pagina = Integer(2, mob_class=Text).to_corner(DL)
        seguir = ArrowTriangleTip(start_angle=0, fill_opacity=1, color=VMobject().color) \
            .to_corner(DR)
        marca = Text("MathLike").to_corner(UL)
        self.add(contenido, pagina, seguir, marca)


class ProductoCartesiano3(Scene):
    def construct(self):
        text = Tex(
            "ejemplo, para ", "$(4, b)$", r""", pues debe respetar\\
            el orden, primero un elemento de """, "$A$",
            r" y\\luego de ", "$B$", ", no al revés.",
            font_size=54, tex_environment=None
        ).set_color_by_tex("$", MATH_GREEN)
        text2 = Tex(
            r"""Así que podemos definir al producto\\
            cartesiano entre """, "$A$", " y ", "$B$",
            r" de la siguiente\\forma:",
            font_size=54, tex_environment=None
        ).set_color_by_tex("$", MATH_GREEN)
        contenido = VGroup(text, text2).arrange(DOWN, aligned_edge=LEFT)
        expr = MathTex(r"A\times B=\{(a,b):a\in A\land b\in B\}", color=WHITE, font_size=66) \
            .next_to(contenido, DOWN, buff=1.5)
        rec = SurroundingRectangle(expr, color=VMobject().color, corner_radius=0.2).set_fill(opacity=1)
        pagina = Integer(3, mob_class=Text).to_corner(DL)
        seguir = ArrowTriangleTip(start_angle=0, fill_opacity=1, color=VMobject().color) \
            .to_corner(DR)
        marca = Text("MathLike").to_corner(UL)
        self.add(rec, contenido, expr, pagina, seguir, marca)


class Final(Scene):
    def construct(self):
        text = Text("¡Suscríbete a mi canal de\nYouTube!", t2c={"YouTube": PURE_RED}, font_size=60)
        logo = Logo().scale(1.5)
        yt = SVGMobject("youtube.svg").scale(0.5).next_to(logo.get_corner(UR), DOWN, aligned_edge=RIGHT, buff=0.5)
        text.next_to(logo, UP)
        text2 = Text("¡Link en mi bio!", t2w={"bio": BOLD}, color=PURE_RED, font_size=60).next_to(logo, DOWN, buff=0.5)
        self.add(text, logo, yt, text2)