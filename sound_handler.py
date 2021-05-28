from pygame import mixer

mixer.init()
footstep = mixer.Sound('sfx/stepdirt_1.wav')
attack = mixer.Sound('sfx/Socapex - new_hits_5.wav')
miss = mixer.Sound('sfx/swosh-20.flac')
heal = mixer.Sound('sfx/heal.wav')
throwable = mixer.Sound('sfx/impact.wav')
toggle = mixer.Sound('sfx/toggle.wav')
explosion = mixer.Sound('sfx/rumble.flac')
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
            if not mixer.music.get_busy():
                mixer.music.load('music/Desolate Hallways.mp3')
                mixer.music.set_volume(0.3)
                mixer.music.play()
        else:
            mixer.music.unload()
            mixer.music.set_volume(0.3)
            mixer.music.load('music/what we make from it.mp3')
            mixer.music.play()