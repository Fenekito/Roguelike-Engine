from pygame import mixer

mixer.init()
footstep = mixer.Sound('stepdirt_1.wav')
attack = mixer.Sound('Socapex - new_hits_5.wav')
miss = mixer.Sound('swosh-20.flac')
heal = mixer.Sound('heal.wav')
throwable = mixer.Sound('impact.wav')
toggle = mixer.Sound('toggle.wav')
explosion = mixer.Sound('rumble.flac')
mixer.Sound.set_volume(attack, 1.3)
mixer.Sound.set_volume(miss, 0.7)

class SoundHandler():
    def handling(state) -> None:
        if state == 'moving':
            mixer.Channel(1).play(mixer.Sound(footstep))
        if state == 'Melee':
            mixer.Channel(0).play(mixer.Sound(attack))
        if state == 'die':
            mixer.Channel(2).play(mixer.Sound(miss))
        if state == 'miss':
            mixer.Channel(2).play(mixer.Sound(miss))

    def ItemHandling(state) -> None:
        if state == 'heal':
            mixer.Channel(3).play(mixer.Sound(heal))
        elif state == 'throwable':
            mixer.Channel(3).play(mixer.Sound(throwable))
        elif state == 'explosive':
            mixer.Channel(3).play(mixer.Sound(explosion))
        elif state == 'toggle':
            mixer.Channel(3).play(mixer.Sound(toggle))

    def BGMHandler(level) -> None:
        if level < 4:
            mixer.music.load('Desolate Hallways.mp3')
            mixer.music.set_volume(0.3)
            mixer.music.play()
        else:
            mixer.music.unload()
            mixer.music.set_volume(0.3)
            mixer.music.load('what we make from it.mp3')
            mixer.music.play()