from pygame import mixer

mixer.init()
footstep = mixer.Sound('')
attack = mixer.Sound('')
miss = mixer.Sound('')
heal = mixer.Sound('')
throwable = mixer.Sound('')
toggle = mixer.Sound('')
explosion = mixer.Sound('')
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
            mixer.Channel.play(mixer.Sound(explosion))
        elif state == 'toggle':
            mixer.Channel(3).play(mixer.Sound(toggle))