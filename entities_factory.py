from components.ai import HostileEnemy
from components.fighter import Fighter
from components.inventory import Inventory
from components import consumable
from entity import Actor, Item
import random

f = open('NAME.txt')
name = f.read()
f.close()

if name == "":
    name = "The Unknown"

player = Actor(
    char="@",
    color=(82, 216, 7),
    name=name,
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
)

decayed = Actor(
    char="D",
    color=(255, 65, 7),
    name="Decayed",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=15, defense=0, power=random.randint(3,4)),
    inventory=Inventory(capacity=0),
    )
mastermind = Actor(
    char="M",
    color=(78, 81, 255),
    name="Mastermind",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=66, defense=12, power=22),
    inventory = Inventory(capacity=0),
)
minormind = Actor(
    char="m",
    color=(0,255,255),
    name="Minormind",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=44, defense=6, power=16),
    inventory=Inventory(capacity=0),
)
jockster = Actor(
    char="J",
    color=(78, 81, 255),
    name="Jockster",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=20, defense=2, power=5),
    inventory=Inventory(capacity=0),
)

bandage = Item(
    char="#",
    color=(127, 0, 255),
    name="Bandage",
    consumable=consumable.HealingConsumable(amount=5),
)
brick = Item(
    char=":",
    color=(240, 104, 83),
    name= "Throwing Brick",
    consumable=consumable.ThrowingBrickDamageConsumable(damage=10, maximum_range=5),
)
"""laser_pointer = Item(
    char="~",
    color=(0,0,0),
    name="disposable pointer",
    consumable=consumable.ConfusionConsumable(number_of_turns=5),
)"""
grenade = Item(
    char="8",
    color=(255, 0, 0),
    name="Grenade",
    consumable=consumable.GrenadeDamageConsumable(damage=12, radius=3),
)