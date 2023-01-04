# Code for ManimCE

from manim import *


def load_mob_default(light_theme=False):
    MathTex.set_default(tex_template=TexTemplate(
        preamble=r"""
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
    ))
    Text.set_default(font="CMU Serif")
    config.max_files_cached = -1
    if light_theme:
        config.background_color = WHITE
        VMobject.set_default(stroke_color=BLACK)