from pygame import mixer

mixer.init()
footstep = mixer.Sound('')
attack = mixer.Sound('')
miss = mixer.Sound('')
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