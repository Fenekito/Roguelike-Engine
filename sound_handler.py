from pygame import mixer
import AudioClip

class SoundHandler():
    def __init__(self) ->None:
        if not mixer.init():
            mixer.init()
            mixer.set_num_channels(32)

    def play(sound : AudioClip):
        channel = mixer.find_channel()
        channel.play(sound.getClip())

    def playBGM(self, sound : str):
        if not mixer.music.get_busy():
            if sound != "music/what we make from it.mp3":
                mixer.music.load(sound)
                mixer.music.set_volume(0.3)
                mixer.music.play(-1)

    def isBusy(self):
        return mixer.music.get_busy()

    def overrideBGM(self, sound : str):
        mixer.music.stop()
        mixer.music.unload()
        mixer.music.load(sound)
        mixer.music.play(-1)