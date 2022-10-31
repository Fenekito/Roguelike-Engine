from __future__ import annotations

import math
from typing import TYPE_CHECKING

import color
from AudioClip import AudioClip
from components.base_component import BaseComponent
from render_order import RenderOrder
from sound_handler import SoundHandler

if TYPE_CHECKING:
    from entity import Actor

class Fighter(BaseComponent):
    parent: Actor

    def __init__(self, hp: int, base_defense: int, base_power: int, hunger: int, max_hunger : int):
        self.max_hp = hp
        self._hp = hp
        self.base_defense = base_defense
        self.base_power = base_power
        self._hunger = hunger
        self.max_hunger = max_hunger
        self.hunger_moves = 15
        self.debuff_moves = 0
        self._debuff = math.floor(self.base_defense / 2)

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.parent.ai:
            self.die()
    @property
    def defense(self) -> int:
        if self.debuff_moves > 0:
            return (self.base_defense + self.defense_bonus) - self.debuff
        else:
            return self.base_defense + self.defense_bonus

    @property
    def power(self) -> int:
        return self.base_power + self.power_bonus

    @property
    def defense_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.defense_bonus
        else:
            return 0

    @property
    def power_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.power_bonus
        else:
            return 0

    @property
    def hunger(self) ->int:
        return self._hunger

    @hunger.setter
    def hunger(self, value: int) -> None:
        self._hunger = max(0, min(value, self.max_hunger))
        if self._hunger == 0 and self.parent.ai:
            self.starve()

    @property
    def debuff(self) -> int:
        return self._debuff

    @debuff.setter
    def debuff(self, value : int) -> None:
        self._debuff = max(0, min(value, math.floor(self.base_defense / 2)))

    def die(self) -> None:
        if self.engine.player is self.parent:
            death_message = "You died!"
            death_message_color = color.player_die
            clip = AudioClip("sfx/swosh-20.flac")
            SoundHandler.play(clip)
        else:
            death_message = f"{self.parent.name} is dead!"
            death_message_color = color.enemy_die
        self.parent.char = "%"
        self.parent.color = (191, 0, 0)
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"dead body of {self.parent.name}"
        self.parent.render_order = RenderOrder.CORPSE
        self.engine.message_log.add_message(death_message, death_message_color)
        self.engine.player.level.add_xp(self.parent.level.xp_given)

    def heal(self, amount: int) -> int:
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp

        self.hp = new_hp_value

        return amount_recovered

    def take_damage(self, amount: int) -> None:
        self.hp -= amount

    def eat(self, amount: int) -> int:
        if self.hunger == self.max_hunger:
            return 0

        new_hunger_value = self.hunger + amount

        if new_hunger_value > self.max_hunger:
            new_hunger_value = self.max_hunger

        amount_recovered = new_hunger_value - self.hunger

        self.hunger = new_hunger_value

        return amount_recovered

    def rest(self) -> None:
        if self.hunger >= 50:
            self.engine.message_log.add_message("You rest a little, lowering your defenses for a while")
            self.hunger -= 25
            self.hp = self.max_hp
            self.debuff_moves = 5

    def starve(self) -> None:
        self.hunger_moves -= 1
        self.debuff_moves -= 1
        if self.hunger_moves <= 0:
            if self.hp < self.max_hp and self.hunger > 65:
                self.hunger -= 2
                self.engine.message_log.add_message(f"Your filled Stomach helped you recover from your wounds", color.health_recovered)
            else:
                self.hunger -= 1
            self.hunger_moves = 15

            """Passive Healing"""
            if self.hunger > 90:
                self.hp += 3
            elif self.hunger > 80:
                self.hp += 2
            elif self.hunger > 65:
                self.hp += 1

        if self.engine.player is self.parent and self._hunger <= 0:
            self.hp -= 1
            self.engine.message_log.add_message(f"You lose 1 hp from starvation!")
            if self._hunger == 0 and self.parent.ai and self._hp == 0:
                self.die()