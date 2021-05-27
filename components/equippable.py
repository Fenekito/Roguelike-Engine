from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
            self,
            equipment_type: EquipmentType,
            power_bonus: int = 0,
            defense_bonus: int = 0,
            health_bonus: int = 0,
    ):
        self.equipment_type = equipment_type

        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.health_bonus = health_bonus


class RustyKnife(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=2)


class BaseballBat(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=4)


class Machete(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=6)


class LeatherJacket(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=1)


class MakeshiftVest(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=3)


class PoliceVest(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=4)


class MilitaryVest(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=7)


class Kimono(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=2, power_bonus=2)


class MakeshiftShield(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, defense_bonus=2, power_bonus=1)


class RiotShield(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, defense_bonus=4, power_bonus=1)


class ArmorSpikes(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ACCESSORY, defense_bonus=1, power_bonus=2)


class ArmsEnhancer(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ACCESSORY, power_bonus=4)


class ArmorPlates(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ACCESSORY, defense_bonus=3)
