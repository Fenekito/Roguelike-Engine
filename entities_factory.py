from components.ai import HostileEnemy, PermConfusedEnemy
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from components.equipment import Equipment
from components import consumable, equippable
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
    equipment=Equipment(),
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, base_defense=2, base_power=5),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=300),
)

rusty = Actor(
    char="R",
    color=(255, 8, 10),
    name="Rusty One",
    equipment=Equipment(),
    ai_cls=PermConfusedEnemy,
    fighter=Fighter(hp=22, base_defense=1, base_power= random.randint(4, 7)),
    inventory= Inventory(capacity=0),
    level=Level(xp_given=35),
)

decayed = Actor(
    char="D",
    color=(255, 65, 7),
    name="Decayed",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=15, base_defense=0, base_power=random.randint(4,5)),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
    )
mastermind = Actor(
    char="M",
    color=(78, 81, 255),
    name="Mastermind",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=66, base_defense=12, base_power=random.randint(22, 48)),
    inventory = Inventory(capacity=0),
    level=Level(xp_given=1000),
)
minormind = Actor(
    char="m",
    color=(0,255,255),
    name="Minormind",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=44, base_defense=6, base_power=random.randint(14, 20)),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=300)
)
jockster = Actor(
    char="J",
    color=(78, 81, 255),
    name="Jockster",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=18, base_defense=2, base_power=random.randint(5, 8)),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=125),
)

bandage = Item(
    char="#",
    color=(127, 0, 255),
    name="Bandage",
    consumable=consumable.HealingConsumable(amount=5),
)

first_aid = Item(
    char="+",
    color=(255,0,0),
    name= "first-aid",
    consumable=consumable.HealingConsumable(amount=30),
)

brick = Item(
    char=":",
    color=(240, 104, 83),
    name= "Throwing Brick",
    consumable=consumable.ThrowingBrickDamageConsumable(damage=10, maximum_range=5),
)
laser_pointer = Item(
    char="~",
    color=(0,0,0),
    name="disposable pointer",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

grenade = Item(
    char="8",
    color=(255, 0, 0),
    name="Grenade",
    consumable=consumable.GrenadeDamageConsumable(damage=12, radius=3),
)

flashbang = Item(
    char="8",
    color=(255,255,255),
    name="Smart Flashbang",
    consumable=consumable.GrenadeConfusionConsumable(number_of_turns=8, radius=3)
)

rknife = Item(
    char="/", color=(0, 191, 255), name="Rusty Knife", equippable=equippable.RustyKnife()
)

BBat = Item(
    char=";", color=(0, 191, 255), name="Baseball Bat", equippable=equippable.BaseballBat()
)

Machete = Item(
    char="|", color=(0, 191, 255), name="Machete", equippable=equippable.Machete()
)

RiotShield = Item(
    char="|",
    color=(135, 65, 16),
    name="Riot Shield",
    equippable=equippable.RiotShield(),
)

LJacket = Item(
    char="(",
    color=(139, 69, 19),
    name="Leather Jacket",
    equippable=equippable.LeatherJacket(),
)

MShiftVest = Item(
    char="[",
    color=(139, 69, 19),
    name="Makeshift Vest",
    equippable=equippable.MakeshiftVest(),
)

PoliceVest = Item(
    char="{",
    color=(135, 65, 16),
    name="Police Vest",
    equippable=equippable.PoliceVest(),
)

MilitaryVest = Item(
    char="=",
    color=(137, 67, 18),
    name="Military Vest",
    equippable=equippable.MilitaryVest(),
)

Kimono = Item(
    char="^",
    color=(125,125,125),
    name="Kimono",
    equippable=equippable.Kimono(),
)

ArmorPlate = Item(
    char="=",
    color=(0,0,0),
    name="Armor Plates",
    equippable=equippable.ArmorPlates(),
)

ArmorSpikes = Item(
    char="<",
    color=(0,0,0),
    name="Armor Spikes",
    equippable=equippable.ArmorSpikes(),
)

ArmsEnhancer = Item(
    char="2",
    color=(0, 208, 255),
    name="Arms Enhancer",
    equippable=equippable.ArmsEnhancer(),
)