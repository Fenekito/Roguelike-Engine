from pygame import mixer

class AudioClip:
    def __init__(self, file : str):
        if not mixer.init():
            mixer.init()

        self.file = file
        self.clip = mixer.Sound(file)

    def getClip(self):
        return self.clip

    def setVolume(self, volume:float) ->None:
        self.clip.set_volume(volume)