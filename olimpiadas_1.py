from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from mob_default import load_mob_default
from logo import Logo
from itertools import permutations


load_mob_default()


class ChileanFlag(SVGMobject):
    def __init__(self):
        super().__init__("_chile.svg")


class Ejercicio(ImageMobject):
    def __init__(self):
        super().__init__("_olimpiada_1.png")


class Thumbnail(Scene):
    def construct(self):
        logo = Logo().scale(0.75).to_corner(DR)
        the_sum = self.generate_sum().scale(2).to_edge(UP)
        br = Brace(the_sum, LEFT)
        plus = MathTex("+", font_size=192)
        br.put_at_tip(plus)
        chile = ChileanFlag().to_corner(UR)
        self.add(logo, the_sum, br, plus, chile)

    def generate_sum(self):
        the_sum = VGroup()
        digits = range(1, 6)
        perms = list(permutations(digits))
        to_use = perms[:5] + [perms[-1]]
        self.parse_digits(to_use)
        
        for item in to_use:
            if item == to_use[-1]:
                the_sum.add(MathTex("\\vdots"))
            the_sum.add(Integer(item))
        
        the_sum.arrange(DOWN)
        return the_sum
    
    def parse_digits(self, to_use, fix_digit=None, digit_order=None):
        for i in range(len(to_use)):
            to_use[i] = list(to_use[i])
            if fix_digit is not None:
                digit_order = digit_order if digit_order is not None else 0
                to_use[i].insert(digit_order, fix_digit)
            for j in range(len(to_use[i])):
                to_use[i][j] *= 10 ** (len(to_use[i])-1-j)
            to_use[i] = sum(to_use[i])


class ElEjercicio(VoiceoverScene):
    def setup(self):
        self.set_speech_service(RecorderService(transcription_model="large"))

    def construct(self):
        ejercicio = Ejercicio()
        olimpiada = Text("Prueba Clasificatoria Olimpiada Nacional de Matemática 1990", font_size=36)
        chile = ChileanFlag()
        Group(olimpiada, ejercicio, chile).arrange(DOWN)
        with self.voiceover("Tenemos este ejercicio de una olimpiada de matemáticas"):
            self.play(Write(olimpiada))
            self.wait_for_voiceover()
        with self.voiceover(
            """Encuentre la suma de los 120 números 12.345, 12.354, 12.435, ...,
            54.321 que resultan de efectuar todas las permutaciones de los cinco
            dígitos 1, 2, 3, 4, 5"""
        ):
            self.play(FadeIn(ejercicio))
            self.wait_for_voiceover()
        with self.voiceover("Este ejercicio es de la olimpiada de Chile. Ahora vamos a resolverlo"):
            self.play(GrowFromCenter(chile))
            self.wait_for_voiceover()


class Resolviendo(VoiceoverScene):
    def setup(self):
        self.set_speech_service(RecorderService(transcription_model="large"))

    def construct(self):
        with self.voiceover(
            """Aquí tenemos la larguísima suma que debemos efectuar, pero aplicaremos
            una estrategia para resolverla"""
        ):
            the_sum = self.generate_sum()
            for item in the_sum:
                if item == the_sum[-4]:
                    self.play(Write(item))
                else:
                    self.play(GrowFromCenter(item))
            self.wait_for_voiceover()
        nums = VGroup(*the_sum[:5], the_sum[-3])
        colors = (YELLOW_A, YELLOW_B, YELLOW_C, YELLOW_D, YELLOW_E)
        with self.voiceover(
            """Vamos a sumar por separado decenas de mil con decenas de mil, unidades de mil
            con unidades de mil, y así para centenas, decenas y unidades para luego sumar todo
            y obtener el resultado esperado"""
        ):
            for i, color in zip((0, 1, 3, 4, 5), colors):
                for num in nums:
                    self.play(num[i].animate(run_time=0.2).scale(1.2).set_color(color))
            self.wait_for_voiceover()
        fijando = Integer(12345)
        with self.voiceover("Con las decenas de mil <bookmark mark='A'/>, fijaré el 1 en la posición"):
            self.play(ReplacementTransform(the_sum, fijando))
            self.wait_until_bookmark("A")
            self.play(fijando[0].animate.scale(1.2).set_color(YELLOW))
            self.wait_for_voiceover()
        digitos = range(2, 6)
        perms = list(permutations(digitos))
        self.parse_digits(perms, fix_digit=1)
        perms_g = VGroup(*[Integer(perm) for perm in perms])
        for perm in perms_g:
            perm[0].scale(1.2).set_color(YELLOW)
        with self.voiceover(
            """Date cuenta que si fijamos el 1 y vamos variando el número con la condición
            de ese 1 fijo, básicamente estamos viendo todas las permutaciones de los dígitos 2, 3, 4 y 5"""
        ):
            for perm in perms_g[1:] + perms_g[0]:
                self.play(Transform(fijando, perm), run_time=0.2)
            self.wait_for_voiceover()
        br = Brace(fijando[1:], DOWN)
        text = br.get_text("Permutaciones")
        with self.voiceover("Entonces son permutaciones de una cierta cantidad de elementos"):
            self.play(Write(br))
            self.play(Write(text))
            self.play(ShowPassingFlash(Underline(text, color=YELLOW)))
            self.wait_for_voiceover()
        fact = MathTex("4!", "=", "24").to_edge(DOWN)
        with self.voiceover("Es un conjunto de cuatro dígitos, es decir, son 4 factorial permutaciones"):
            self.play(Write(fact[0]))
            self.wait_for_voiceover()
        with self.voiceover("Es decir, son 24 permutaciones"):
            self.play(Write(fact[1:]))
            self.wait_for_voiceover()
        primera_parte = MathTex("10,000", "\\cdot", "24").next_to(fijando, DOWN)
        with self.voiceover(
            """¿Y qué significa esto? Significa que para la decena de mil igual a 1 tenemos
            24 posibilidades, es decir, <bookmark mark='A'/>la primera parte de la suma de decenas de mil
            será decena de mil, o sea 10000, por 24"""
        ):
            self.wait_until_bookmark("A")
            self.play(Unwrite(VGroup(br, text)))
            self.play(GrowFromCenter(primera_parte))
            self.wait_for_voiceover()
        with self.voiceover("Ahora cambiaremos nuestra decena de mil fija, ahora será 2"):
            self.play(fijando[0].animate.scale(5/6).set_color(WHITE), FadeOut(fact, shift=DOWN))
            fijando_2 = Integer(21234)
            self.play(Transform(fijando, fijando_2))
            self.play(fijando[0].animate.scale(1.2).set_color(YELLOW))
            self.wait_for_voiceover()
        digitos = (1, 3, 4, 5)
        perms = list(permutations(digitos))
        self.parse_digits(perms, fix_digit=2)
        perms_g = VGroup(*[Integer(perm) for perm in perms])
        for perm in perms_g:
            perm[0].scale(1.2).set_color(YELLOW)
        with self.voiceover("Si variamos el resto de los dígitos, vamos de nuevo a obtener que son permutaciones"):
            for perm in perms_g[1:] + perms_g[0]:
                self.play(Transform(fijando, perm), run_time=0.2)
            self.wait_for_voiceover()
        br = Brace(fijando[1:], DOWN)
        text = br.get_text("Permutaciones")
        with self.voiceover("Entonces necesitamos la cantidad de dígitos que se permutan"):
            self.play(FadeOut(primera_parte))
            self.play(Write(br))
            self.play(Write(text))
            self.play(ShowPassingFlash(Underline(text, color=YELLOW)))
            self.wait_for_voiceover()
        fact = MathTex("4!", "=", "24").to_edge(DOWN)
        with self.voiceover("Y como son 4 dígitos, serían 4 factorial permutaciones"):
            self.play(Write(fact[0]))
            self.wait_for_voiceover()
        with self.voiceover("Es decir, 24 permutaciones"):
            self.play(Write(fact[1:]))
            self.wait_for_voiceover()
        segunda_parte = MathTex("10,000", "\\cdot", "24", "+", "20,000", "\\cdot", "24").next_to(fijando, DOWN)
        with self.voiceover("Ahora vamos a volver a la suma que teníamos"):
            self.play(Unwrite(VGroup(br, text)))
            self.play(FadeIn(primera_parte))
            self.wait_for_voiceover()
        with self.voiceover(
            """Teníamos que eran 10000 por 24, ahora le vamos a sumar <bookmark mark='A'/> las dos decenas de mil, 20000,
            eso por 24"""
        ):
            self.wait_until_bookmark("A")
            self.play(TransformMatchingTex(primera_parte, segunda_parte))
            self.wait_for_voiceover()
        with self.voiceover("Ahora vamos viendo que se cumple un patrón"):
            self.play(FadeOut(fijando, fact), segunda_parte.animate.center())
            self.wait_for_voiceover()
        tercera_parte = MathTex("10,000", "\\cdot", "24", "+", "20,000", "\\cdot", "24", "+", "\\ldots", "+", "50,000", "\\cdot", "24")
        with self.voiceover(
            """Esto se va a seguir cumpliendo hasta las cinco decenas de mil, <bookmark mark='A'/>por lo que
            el último sumando para decenas de mil sería 50000 por 24"""
        ):
            self.wait_until_bookmark("A")
            self.play(TransformMatchingTex(segunda_parte, tercera_parte))
            self.wait_for_voiceover()
        cuarta_parte = MathTex("10,000", "\\cdot", "(1+2+3+4+5)", "\\cdot", "24")
        with self.voiceover("Ahora sacaremos factor común 10000, quedando esto"):
            self.play(TransformMatchingTex(tercera_parte, cuarta_parte))
            self.wait_for_voiceover()
        quinta_parte = MathTex("10,000", "\\cdot", "15", "\\cdot", "24")
        with self.voiceover("Y la suma 1+2+3+4+5 es igual a 15"):
            self.play(TransformMatchingTex(cuarta_parte, quinta_parte))
            self.wait_for_voiceover()
        self.play(FadeOut(quinta_parte))
        fijando = Integer(21345)
        with self.voiceover("Ahora vamos con las unidades de mil y fijaré el 1"):
            self.play(GrowFromCenter(fijando))
            self.play(fijando[1].animate.scale(1.2).set_color(YELLOW))
            self.wait_for_voiceover()
        digitos = range(2, 6)
        perms = list(permutations(digitos))
        self.parse_digits(perms, fix_digit=1, digit_order=1)
        perms_g = VGroup(*[Integer(perm) for perm in perms])
        for perm in perms_g:
            perm[1].scale(1.2).set_color(YELLOW)
        with self.voiceover("De igual manera que antes, tendremos permutaciones entre cuatro dígitos"):
            for perm in perms_g[1:] + perms_g[0]:
                self.play(Transform(fijando, perm), run_time=0.2)
            self.wait_for_voiceover()
        fact = MathTex("4!", "=", "24").to_edge(DOWN)
        with self.voiceover("O sea, como tenemos 4 dígitos variando, es 4 factorial"):
            self.play(Write(fact[0]))
            self.wait_for_voiceover()
        with self.voiceover("Es decir, 24 posibilidades"):
            self.play(Write(fact[1:]))
        sexta_parte = MathTex("10,000", "\\cdot", "15", "\\cdot", "24", "+", "1,000", "\\cdot", "24") \
            .next_to(fijando, DOWN)
        quinta_parte.next_to(fijando, DOWN)
        self.play(FadeIn(quinta_parte))
        with self.voiceover("Como estamos en unidades de mil, le sumamos una unidad de mil, es decir, 1000, eso por 24"):
            self.play(TransformMatchingTex(quinta_parte, sexta_parte))
            self.wait_for_voiceover()
        self.play(FadeOut(fijando, fact), sexta_parte.animate.center())
        septima_parte = MathTex("10,000", "\\cdot", "15", "\\cdot", "24", "+", "1,000", "\\cdot", "24", "+", "\\ldots", "+", "5,000", "\\cdot", "24")
        with self.voiceover("Eso se cumplirá para el resto de unidades de mil también, por lo que hay hasta 5000 por 24"):
            self.play(TransformMatchingTex(sexta_parte, septima_parte))
            self.wait_for_voiceover()
        octava_parte = MathTex("10,000", "\\cdot", "15", "\\cdot", "24", "+", "1,000", "\\cdot", "(1+2+3+4+5)", "\\cdot", "24")
        with self.voiceover("Factorizamos por 1000 a la derecha"):
            self.play(TransformMatchingTex(septima_parte, octava_parte))
            self.wait_for_voiceover()
        novena_parte = MathTex("10,000", "\\cdot", "15", "\\cdot", "24", "+", "1,000", "\\cdot", "15", "\\cdot", "24")
        with self.voiceover("1+2+3+4+5 es 15"):
            self.play(TransformMatchingTex(octava_parte, novena_parte))
            self.wait_for_voiceover()
        decima_parte = MathTex("(10,000+1,000)", "\\cdot", "15", "\\cdot", "24")
        with self.voiceover("Factorizamos por 15 por 24"):
            self.play(TransformMatchingTex(novena_parte, decima_parte))
            self.wait_for_voiceover()
        onceava_parte = MathTex("(10,000+1,000+100+10+1)", "\\cdot", "15", "\\cdot", "24")
        with self.voiceover(
            """Identificando el patrón que se forma, <bookmark mark='A'/>añadimos las centenas,
            decenas y unidades, o sea 100, 10 y 1"""
        ):
            self.wait_until_bookmark("A")
            self.play(TransformMatchingTex(decima_parte, onceava_parte))
            self.wait_for_voiceover()
        doceava_parte = MathTex("11111", "\\cdot", "15", "\\cdot", "24")
        with self.voiceover("La suma entre paréntesis equivale a 11111"):
            self.play(TransformMatchingTex(onceava_parte, doceava_parte))
            self.wait_for_voiceover()
        resultado_final = MathTex(f"{11111*15*24}").scale(2)
        with self.voiceover(f"O sea, tenemos el resultado final: <bookmark mark='A'/> es {11111*15*24}"):
            self.play(FadeOut(doceava_parte))
            self.wait_until_bookmark("A")
            self.play(GrowFromCenter(resultado_final))
            self.wait_for_voiceover()
        self.play(Circumscribe(resultado_final))

    def generate_sum(self):
        the_sum = VGroup()
        digits = range(1, 6)
        perms = list(permutations(digits))
        to_use = perms[:5] + [perms[-1]]
        self.parse_digits(to_use)
        
        for item in to_use:
            if item == to_use[-1]:
                the_sum.add(MathTex("\\vdots"))
            the_sum.add(Integer(item))
        
        the_sum.arrange(DOWN)
        plus_symbol = MathTex("+").next_to(the_sum[-1], LEFT)
        line = Line(VGroup(the_sum[-1], plus_symbol).get_corner(DL), VGroup(the_sum[-1], plus_symbol).get_corner(DR)) \
            .shift(SMALL_BUFF * DOWN)
        the_sum.add(plus_symbol, line)
        the_sum.center()
        return the_sum
    
    def parse_digits(self, to_use, fix_digit=None, digit_order=None):
        for i in range(len(to_use)):
            to_use[i] = list(to_use[i])
            if fix_digit is not None:
                digit_order = digit_order if digit_order is not None else 0
                to_use[i].insert(digit_order, fix_digit)
            for j in range(len(to_use[i])):
                to_use[i][j] *= 10 ** (len(to_use[i])-1-j)
            to_use[i] = sum(to_use[i])