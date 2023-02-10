from __future__ import annotations
from manim.scene.scene import Scene
import os
import sys


class VoiceoverManager:
    def __init__(self, scene: VoiceoverScene, subtitulo: str) -> None:
        self.scene = scene
        self.subtitulo = subtitulo
    
    def __enter__(self):
        self.scene.record_audio(self.subtitulo)
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.scene.wait_until_finished()


class VoiceoverScene(Scene):
    def setup(self):
        self.audio_n = 1
        self.music_initial_t = 0
        self.voiceover_folder = os.path.splitext(sys.argv[1])[0]
        self.voiceover_folder = os.path.splitext(os.path.basename(self.voiceover_folder))[0]
        self.voiceover_folder = os.path.join(self.voiceover_folder, self.__class__.__name__)
        self.voiceover_file_base = self.__class__.__name__

    def record_audio(self, subtitulo: str):
        import sounddevice as sd
        from scipy.io.wavfile import write
        import time

        fs = 44100
        seconds = 150
        filename = self.voiceover_file_base + str(self.audio_n) + ".wav"
        folder = self.voiceover_folder
        parent = os.path.dirname(folder)
        filename = os.path.join("media", folder, filename)
        if not os.path.exists(os.path.join("media", parent)):
            os.mkdir(os.path.join("media", parent))
        if not os.path.exists(os.path.join("media", folder)):
            os.mkdir(os.path.join("media", folder))
        if not os.path.exists(filename):
            input(subtitulo.replace(4 * " ", "") + "\n")
            print("Grabando en 1 segundo")
            time.sleep(1)
            print("Grabando (el último segundo será eliminado del audio)")
            t = 0
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            while True:
                try:
                    time.sleep(1 / self.camera.frame_rate)
                    t += 1 / self.camera.frame_rate
                except KeyboardInterrupt:
                    sd.stop()
                    break
            print("Terminado")
            write(filename, fs, myrecording[:int((t - 1) * fs)])
        else:
            from pydub import AudioSegment

            audio = AudioSegment.from_wav(filename)
            t = len(audio) / 1000
        now = self.renderer.time
        self.t = lambda: now - self.renderer.time + t
        self.add_sound(filename)
        self.audio_n += 1
        self.wait_until_finished = lambda: self.wait(self.t()) if now - self.renderer.time + t >= 1 / self.camera.frame_rate else None
    
    def add_music(self, filename: str, gain: float = -35):
        from pydub import AudioSegment

        trimmed_filename = f"{os.path.splitext(filename)[0]}_trimmed.mp3"
        filename = os.path.join("media", self.voiceover_folder, filename)
        trimmed_filename = os.path.join("media", self.voiceover_folder, trimmed_filename)
        song = AudioSegment.from_mp3(filename)
        trimmed_song = song[:int(self.renderer.time * 1000)] if int(self.renderer.time * 1000) < len(song) else song
        trimmed_song.export(trimmed_filename, format="mp3")
        self.add_sound(trimmed_filename, time_offset=-self.renderer.time + self.music_initial_t, gain=gain)
        self.music_initial_t = len(trimmed_song) / 1000
    
    def voiceover(self, subtitulo: str):
        return VoiceoverManager(self, subtitulo)