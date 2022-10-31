from pygame import mixer

import AudioClip


class SoundHandler():
    def __init__(self) ->None:
        if not mixer.init():
            mixer.init()
            mixer.set_num_channels(48)

    def play(sound : AudioClip):
        channel = mixer.find_channel()
        channel.play(sound.getClip())

        return channel

    def playSeamless(sound: AudioClip, channel:int):
        if not mixer.Channel(channel).get_busy():
            mixer.Channel(channel).play(sound.getClip())

    def playSeamless(sound: AudioClip, channel:int):
        if not mixer.Channel(channel).get_busy():
            mixer.Channel(channel).play(sound.getClip())

    def playLooped(sound: AudioClip):
        channel = mixer.find_channel()
        channel.play(sound.getClip(), -1)

    def isPlaying(channel: mixer.Channel):
        return channel.get_busy()

    def playBGM(self, sound : str, override : bool):
        if not mixer.music.get_busy() or override:
            mixer.music.load(sound)
            mixer.music.set_volume(0.3)
            mixer.music.play(-1)

    def isBusy(self):
        return mixer.music.get_busy()