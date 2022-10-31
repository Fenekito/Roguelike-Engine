from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import actions
import color
import components.ai
import components.inventory
from AudioClip import AudioClip
from components.base_component import BaseComponent
from exceptions import Impossible
from input_handlers import (
    ActionOrHandler,
    AreaRangedAttackHandler,
    SingleRangedAttackHandler,
)
from sound_handler import SoundHandler

if TYPE_CHECKING:
    from entity import Actor, Item


class Consumable(BaseComponent):
    parent: Item

    def get_action(self, consumer: Actor) -> Optional[ActionOrHandler]:
        """Try to return the action for this item."""
        return actions.ItemAction(consumer, self.parent)

    def activate(self, action: actions.ItemAction) -> None:
        """Invoke this items ability.

        `action` is the context for this activation.
        """
        raise NotImplementedError()

    def consume(self) -> None:
        """Remove the consumed item from its containing inventory."""
        entity = self.parent
        inventory = entity.parent
        if isinstance(inventory, components.inventory.Inventory):
            inventory.items.remove(entity)

class ConfusionConsumable(Consumable):
    def __init__(self, number_of_turns: int):
        self.number_of_turns = number_of_turns

    def get_action(self, consumer: Actor) -> SingleRangedAttackHandler:
        self.engine.message_log.add_message(
            "Select a target location.", color.needs_target
        )
        return SingleRangedAttackHandler(
            self.engine,
            callback=lambda xy: actions.ItemAction(consumer, self.parent, xy),
        )

    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        target = action.target_actor

        if not self.engine.game_map.visible[action.target_xy]:
            raise Impossible("I can't target what I can't see.")
        if not target:
            raise Impossible("No one is close to the effective range")
        if target is consumer:
            raise Impossible("I'm not this dumb.")

        self.engine.message_log.add_message(
            f"The {target.name} has been blinded",
            color.status_effect_applied,
        )
        target.ai = components.ai.ConfusedEnemy(
            entity=target, previous_ai=target.ai, turns_remaining=self.number_of_turns,
        )
        self.consume()
        clip = AudioClip('sfx/toggle.wav')
        SoundHandler.play(clip)

class HealingConsumable(Consumable):
    def __init__(self, amount: int):
        self.amount = amount

    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        amount_recovered = consumer.fighter.heal(self.amount)
        if amount_recovered > 0:
            self.engine.message_log.add_message(
                f"You consume the {self.parent.name}, and recover {amount_recovered} HP!",
                color.health_recovered,
            )
            self.consume()
            clip = AudioClip('sfx/heal.wav')
            SoundHandler.play(clip)
        else:
            raise Impossible(f"Can't heal what's not hurt")

class FoodConsumable(Consumable):
    def __init__(self, amount: int):
        self.amount = amount

    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        amount_recovered = consumer.fighter.eat(self.amount)
        consumer.fighter.hunger_moves = 25 #Makes it so the player has a few extra moves before losing hunger points
        if amount_recovered > 0:
            self.engine.message_log.add_message(
                f"You eat the {self.parent.name}, and fill your hunger by {amount_recovered}!",
                color.health_recovered,
            )
            self.consume()
            clip = AudioClip('sfx/crunch.2.ogg')
            SoundHandler.play(clip)
        else:
            raise Impossible(f"I'm full")

class GrenadeDamageConsumable(Consumable):
    def __init__(self, damage: int, radius: int):
        self.damage = damage
        self.radius = radius

    def get_action(self, consumer: Actor) -> AreaRangedAttackHandler:
        self.engine.message_log.add_message(
            "Select a target location.", color.needs_target
        )
        return AreaRangedAttackHandler(
            self.engine,
            radius=self.radius,
            callback=lambda xy: actions.ItemAction(consumer, self.parent, xy),
        )

    def activate(self, action: actions.ItemAction) -> None:
        target_xy = action.target_xy

        if not self.engine.game_map.visible[target_xy]:
            raise Impossible("I can't target what I can't see.")

        targets_hit = False
        for actor in self.engine.game_map.actors:
            if actor.distance(*target_xy) <= self.radius:
                self.engine.message_log.add_message(
                    f"The {actor.name} is engulfed in a fiery explosion, taking {self.damage} damage!"
                )
                actor.fighter.take_damage(self.damage)
                targets_hit = True

        if not targets_hit:
            raise Impossible("No one is close to the effective range")
        self.consume()
        clip = AudioClip('sfx/rumble.flac')
        SoundHandler.play(clip)

class GrenadeConfusionConsumable(Consumable):
    """
    The player is not affected sadly.
    """

    def __init__(self, number_of_turns: int, radius: int):
        self.number_of_turns = number_of_turns
        self.radius = radius

    def get_action(self, consumer: Actor) -> AreaRangedAttackHandler:
        self.engine.message_log.add_message(
            "Select a target location.", color.needs_target
        )
        return AreaRangedAttackHandler(
            self.engine,
            radius=self.radius,
            callback=lambda xy: actions.ItemAction(consumer, self.parent, xy),
        )

    def activate(self, action: actions.ItemAction) -> None:
        target_xy = action.target_xy
        consumer = action.entity

        if not self.engine.game_map.visible[target_xy]:
            raise Impossible("I can't target what I can't see.")

        targets_hit = False
        for actor in self.engine.game_map.actors:
            if actor.distance(*target_xy) <= self.radius:
                if not actor is consumer:
                    self.engine.message_log.add_message(
                        f"The {actor.name} is flashed",color.status_effect_applied,
                    )
                targets_hit = True
                actor.ai = components.ai.ConfusedEnemy(
                    entity=actor, previous_ai=actor.ai, turns_remaining=self.number_of_turns,
                )

        if not targets_hit:
            raise Impossible("No one is close to the effective range")
        self.consume()
        clip = AudioClip('sfx/rumble.flac')
        SoundHandler.play(clip)

class ThrowingBrickDamageConsumable(Consumable):
    def __init__(self, damage: int, maximum_range: int):
        self.damage = damage
        self.maximum_range = maximum_range

    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        target = None
        closest_distance = self.maximum_range + 1.0

        for actor in self.engine.game_map.actors:
            if actor is not consumer and self.parent.gamemap.visible[actor.x, actor.y]:
                distance = consumer.distance(actor.x, actor.y)

                if distance < closest_distance:
                    target = actor
                    closest_distance = distance

        if target:
            self.engine.message_log.add_message(
                f"A brick was thrown at {target.name}, breaking on impact and dealing {self.damage} damage."
            )
            target.fighter.take_damage(self.damage)
            self.consume()
            clip = AudioClip('sfx/impact.wav')
            SoundHandler.play(clip)
        else:
            raise Impossible("There's no one close enough to get bricked.")