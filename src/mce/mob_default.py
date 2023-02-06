# Code for ManimCE

from manim import *


def load_mob_default(
    light_theme=False,
    shorts=False,
    square=False,
    background_color=None,
    text_font="CMU Serif",
    vmob_default_color=None,
    custom_font_tex=None
):
    if custom_font_tex is None:
        preamble = r"""
\usepackage[spanish]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{dsfont}
\usepackage{setspace}
\usepackage{tipa}
\usepackage{relsize}
\usepackage{textcomp}
\usepackage{mathrsfs}
\usepackage{calligra}
\usepackage{wasysym}
\usepackage{ragged2e}
\usepackage{physics}
\usepackage{xcolor}
\usepackage{microtype}
\usepackage{icomma}
\DisableLigatures{encoding = *, family = * }
\linespread{1}"""
        tex_compiler = "latex"
        output_format = ".dvi"
    else:
        preamble = """
\\usepackage[spanish]{babel}
\\usepackage{fontspec}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{microtype}
\\setmainfont{%s}
\\linespread{1}""" % custom_font_tex
        tex_compiler = "xelatex"
        output_format = ".xdv"
    MathTex.set_default(tex_template=TexTemplate(tex_compiler=tex_compiler, preamble=preamble, output_format=output_format))
    Text.set_default(font=text_font)
    config.max_files_cached = -1
    if light_theme:
        config.background_color = WHITE
        VMobject.set_default(color=BLACK)
    
    if shorts:
        config.pixel_width, config.pixel_height = config.pixel_height, config.pixel_width
        config.frame_height = 16 / 9 * config.frame_width
    
    if square:
        config.pixel_width, config.pixel_height = 2000, 2000
        config.frame_height = config.frame_width
    
    if background_color:
        config.background_color = background_color

    if vmob_default_color is not None:
        VMobject.set_default(color=vmob_default_color)
    
    NumberPlane.set_default(x_range=[-config.frame_x_radius, config.frame_x_radius, 1], y_range=[-config.frame_y_radius, config.frame_y_radius, 1])
    TracedPath.set_default(stroke_color=VMobject().color)
    Dot.set_default(color=VMobject().color)
    Rectangle.set_default(color=BLACK)