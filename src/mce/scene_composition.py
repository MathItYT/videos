from manim.scene.scene import Scene
from voiceover import VoiceoverScene
from typing import Iterable


class SceneComposition(Scene):
    scenes: list

    def construct(self):
        for scene in self.scenes:
            self.subscene_setup(scene)
            scene.construct(self)
            self.remove(*self.mobjects)
    
    def subscene_setup(self, scene):
        pass

class VoiceoverComposition(SceneComposition, VoiceoverScene):
    music_files: list = []
    def subscene_setup(self, scene):
        import os
        import inspect
        self.voiceover_folder = inspect.getmodule(scene).__file__
        self.voiceover_folder = os.path.splitext(os.path.basename(self.voiceover_folder))[0]
        self.voiceover_folder = os.path.join(self.voiceover_folder, scene.__name__)
        self.voiceover_file_base = scene.__name__
        self.audio_n = 1
    
    def construct(self):
        super().construct()
        for music_file in self.music_files:
            if isinstance(music_file, Iterable):
                self.add_music(music_file[0], gain=music_file[1])
            else:
                self.add_music(music_file)