from manim import *
from voiceover import VoiceoverScene
from producto_cartesiano_ig import Final
from custom_animations import GrowEachCharText
import os
from logo import Logo
from mob_default import load_mob_default


load_mob_default(
    light_theme=True, background_color=WHITE, shorts=True, text_font="Poppins", vmob_default_color="#1f284f",
    custom_font_tex="Poppins"
)


class Relaciones(VoiceoverScene):
    def construct(self):
        with self.voiceover("En este video"):
            text = Text("En este video", font_size=96)
            self.play(GrowEachCharText(text), run_time=self.t())
        
        with self.voiceover("Vas a aprender sobre relaciones"):
            txt = "Vas a aprender\nsobre relaciones"
            text2 = Text(txt, font_size=96)
            text3 = Text(txt, t2c={"relaciones": PURE_GREEN}, font_size=96)
            self.play(TransformMatchingShapes(text, text2), run_time=self.t() - 1)
            self.play(Transform(text2, text3), run_time=1)
        
        with self.voiceover("Pero en matemáticas"):
            titulo = Text("Relaciones", font_size=96).to_edge(UP)
            self.play(Transform(text2, titulo))
        
        with self.voiceover("En mi post anterior hablé del producto cartesiano"):
            img_name = "ProductoCartesiano1_ManimCE_v0.17.2.png"
            img = ImageMobject(os.path.join("media", "images", "producto_cartesiano_ig", img_name)) \
                .scale_to_fit_width(config.frame_width - 1)
            rec = SurroundingRectangle(img, buff=0, color=VMobject().color)
            self.play(FadeIn(img), Create(rec))
        
        with self.voiceover("Si no sabes lo que es, ve allá, porque usaremos ese conocimiento"):
            self.play(Indicate(Group(img, rec)))
            self.wait()
            self.play(FadeOut(img), Uncreate(rec))
        
        with self.voiceover("Una relación binaria es simplemente un subconjunto de un producto cartesiano"):
            def_r = MathTex(r"R\subseteq A\times B", font_size=96)
            self.play(Write(def_r))
        
        with self.voiceover(
            """O sea, tomamos cierta parte del producto cartesiano y nos resultarán
            varios pares que estarán relacionados, por eso lo definimos así"""
        ):
            def_r_2 = MathTex(r"R=\{(a,b)\in A\times B:R(a,b)\}", font_size=96)
            self.play(Transform(def_r, def_r_2))
        
        with self.voiceover("Tú seguramente te preguntas qué significa esto de acá"):
            a_R_b = def_r[0][-7:-1]
            br = Brace(a_R_b, DOWN)
            expl = Text("*")
            br.put_at_tip(expl)
            self.play(Write(br), Write(expl))
        
        with self.voiceover("Lo explicaré con un ejemplo"):
            self.play(VGroup(def_r, br, expl).animate.set_opacity(0))
        
        with self.voiceover("Tengo una relación de pares (x, y) en R2 tal que x es y al cuadrado"):
            r = MathTex(r"R=\{(x,y)\in\mathbb{R}^2:x=y^2\}", font_size=96)
            self.play(GrowEachCharText(r))
        
        with self.voiceover("R2 es el producto cartesiano de R por sí mismo, o sea es un par ordenado de números reales"):
            self.play(ShowPassingFlash(Underline(r, color=YELLOW)))
        
        with self.voiceover("Yo sé que (4, 2) pertenece a esta relación, pues 4 es 2^2"):
            ex = MathTex(r"(4,2)\in R", font_size=96).next_to(r, DOWN)
            self.play(GrowEachCharText(ex))
        
        with self.voiceover("También (9, -3) pertenece a R, porque -3 al cuadrado me da 9"):
            ex2 = MathTex(r"(9,-3)\in R", font_size=96).next_to(r, DOWN)
            self.play(Transform(ex, ex2))
        
        with self.voiceover("Sin embargo, esto lo puedo escribir también como R(9, -3), que quiere decir 9 se relaciona con -3"):
            ex3 = MathTex("R(9,-3)", font_size=96).next_to(r, DOWN)
            self.play(FadeTransform(ex, ex3))
        
        with self.voiceover("O sea que esa notación que se lee R(a, b) quiere decir a se relaciona con b"):
            self.play(FadeOut(ex3, r))
            self.play(VGroup(def_r, br, expl).animate.set_opacity(1))
            expl_text = Tex("* $a$ se relaciona con $b$", font_size=96).next_to(expl, DOWN).set_x(0)
            self.play(GrowEachCharText(expl_text))
        
        with self.voiceover("Te dejo como ejercicio algo que te va a servir para el siguiente video que suba a Instagram"):
            self.play(FadeOut(def_r, br, expl, expl_text))
        
        with self.voiceover("Tenemos la misma relación de antes"):
            rel = MathTex(r"R=\{(x,y)\in\mathbb{R}^2:x=y^2\}", font_size=96)
            self.play(GrowEachCharText(rel))
        
        with self.voiceover(
            """Quiero que encuentres el conjunto A de todos los x que se les pueda relacionar
            algún número y en la relación R"""
        ):
            a = MathTex(r"A=\{x\in\mathbb{R}:\exists y,R(x, y)\}", font_size=96).next_to(rel, DOWN, buff=1)
            self.play(GrowEachCharText(a))
        
        with self.voiceover("Te doy una pista. ¿Estará -3 en A? O sea, ¿existiría un y que al cuadrado me de -3?"):
            tex = Tex(r"¿$-3\in A$?", font_size=96).next_to(a, DOWN, buff=1)
            self.play(GrowEachCharText(tex))
        
        with self.voiceover("Recuerda suscribirte a mi canal y chau"):
            self.play(FadeOut(*self.mobjects))
            Final.construct(self)
            mobs = self.mobjects
            self.remove(*mobs)
            self.play(GrowEachCharText(VGroup(*mobs)))


class Portada(Scene):
    def construct(self):
        text = Text("¿Qué son las\nrelaciones binarias?", font_size=96) \
            .set_color_by_gradient(PURE_RED, ORANGE)
        logo = Logo().scale(2).to_corner(DR)
        yt = SVGMobject("youtube.svg").to_corner(UL)
        form = MathTex(r"(x,y)\in R", font_size=240)
        VGroup(text, form).arrange(DOWN, buff=1)
        self.add(text, form, logo, yt)