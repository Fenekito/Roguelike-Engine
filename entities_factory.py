import random

from components import consumable, equippable
from components.ai import HostileEnemy, PermConfusedEnemy
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

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
    fighter=Fighter(hp=30, base_defense=2, base_power=5, max_hunger=100, hunger=100),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=300),
)

rusty = Actor(
    char="R",
    color=(255, 65, 7),
    name="Rusty One",
    equipment=Equipment(),
    ai_cls=PermConfusedEnemy,
    fighter=Fighter(hp=22, base_defense=1, base_power= random.randint(4, 7), max_hunger=1000, hunger=1000),
    inventory= Inventory(capacity=0),
    level=Level(xp_given=50),
)

brknRobot = Actor(
    char="D",
    color=(200, 8, 10),
    name="Broken Drill Robot",
    equipment=Equipment(),
    ai_cls=PermConfusedEnemy,
    fighter=Fighter(hp=30, base_defense=3, base_power=random.randint(4, 10), max_hunger=1000, hunger=1000),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=200),
)

DrillRobot = Actor(
    char="D",
    color=(255, 8, 10),
    name="Drill Robot",
    equipment=Equipment(),
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=40, base_defense=5, base_power=random.randint(7, 12), max_hunger=1000, hunger=1000),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=250),
)

Abomination = Actor(
    char="A",
    color=(0,0,0),
    name="The Abomination",
    equipment=Equipment(),
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=150, base_defense=18, base_power=random.randint(32, 70), max_hunger=1000, hunger=1000),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=5000)
)

experiment = Actor(
    char="E",
    color=(0, 125, 0),
    name=("Experiment"),
    equipment=Equipment(),
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=22, base_defense=2, base_power=random.randint(6, 9), max_hunger=1000, hunger=1000),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=200)
)

decayed = Actor(
    char="D",
    color=(0, 125, 0),
    name="Decayed",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=15, base_defense=0, base_power=random.randint(4,5), max_hunger=1000, hunger=1000),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)

lostHmn = Actor(
    char="H",
    color=(100, 125, 0),
    name="Lost Human",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=15, base_defense=2, base_power=random.randint(4, 6), max_hunger=1000, hunger=1000),
    inventory= Inventory(capacity=0),
    level=Level(xp_given=100)
)

CorruptHuman = Actor(
    char="H",
    color=(0,0,0),
    name="Corrupted Human",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=20, base_defense=1, base_power=random.randint(6, 7), max_hunger=1000, hunger=1000),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=125)
)

mastermind = Actor(
    char="M",
    color=(78, 81, 255),
    name="Mastermind",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=66, base_defense=12, base_power=random.randint(22, 48), max_hunger=1000, hunger=1000),
    inventory = Inventory(capacity=0),
    level=Level(xp_given=2500),
)

minormind = Actor(
    char="m",
    color=(0,255,255),
    name="Minormind",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=44, base_defense=5, base_power=random.randint(14, 20), max_hunger=1000, hunger=1000),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=1000)
)
jockster = Actor(
    char="M",
    color=(0, 125, 0),
    name="Mutated",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=18, base_defense=2, base_power=random.randint(5, 8), max_hunger=1000, hunger=1000),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=150),
)

bandage = Item(
    char="#",
    color=(255,0,0),
    name="Bandage",
    consumable=consumable.HealingConsumable(amount=10),
)

burguer = Item(
    char="B",
    color=(255,125,0),
    name="Burguer",
    consumable=consumable.FoodConsumable(amount=10),
)

nugget = Item(
    char="N",
    color=(255,125,0),
    name="Chicken Nugget",
    consumable=consumable.FoodConsumable(amount=5)
)

noodles = Item(
    char="~",
    color=(255,125,0),
    name="instant Noodles",
    consumable=consumable.FoodConsumable(amount=15)
)

cCake = Item(
    char="C",
    color=(255,125,0),
    name="Chocolate Cake",
    consumable=consumable.FoodConsumable(amount=45)
)

pie = Item(
    char="P",
    color=(255,125,0),
    name="Apple Pie",
    consumable=consumable.FoodConsumable(amount=25)
)

bandaid = Item(
    char="B",
    color=(255,0,0),
    name="Band-Aid",
    consumable=consumable.HealingConsumable(amount=5)
)

first_aid = Item(
    char="+",
    color=(255,0,0),
    name= "First-aid",
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
    name="Disposable pointer",
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
    color=(125,125,125),
    name="Smart Flashbang",
    consumable=consumable.GrenadeConfusionConsumable(number_of_turns=8, radius=3)
)

rknife = Item(
    char="/",
    color=(0, 191, 255),
    name="Rusty Knife",
    equippable=equippable.RustyKnife()
)

BBat = Item(
    char=";",
    color=(0, 191, 255),
    name="Baseball Bat",
    equippable=equippable.BaseballBat()
)

Machete = Item(
    char="|",
    color=(0, 191, 255),
    name="Machete",
    equippable=equippable.Machete()
)

Axe = Item(
    char="F",
    color=(0, 191, 255),
    name="Fire Axe",
    equippable=equippable.Axe()
)

MShiftShield = Item(
    char="(",
    color=(135, 65, 16),
    name="Makeshift Shield",
    equippable=equippable.MakeshiftShield(),
)

RiotShield = Item(
    char="[",
    color=(135, 65, 16),
    name="Riot Shield",
    equippable=equippable.RiotShield(),
)

LJacket = Item(
    char=")",
    color=(139, 69, 19),
    name="Leather Jacket",
    equippable=equippable.LeatherJacket(),
)

MShiftVest = Item(
    char="]",
    color=(139, 69, 19),
    name="Makeshift Vest",
    equippable=equippable.MakeshiftVest(),
)

PoliceVest = Item(
    char="}",
    color=(130, 60, 15),
    name="Police Vest",
    equippable=equippable.PoliceVest(),
)

MilitaryVest = Item(
    char="=",
    color=(130, 60, 15),
    name="Military Vest",
    equippable=equippable.MilitaryVest(),
)

Kimono = Item(
    char="^",
    color=(130, 60, 15),
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
    color=(0,0,0),
    name="Arms Enhancer",
    equippable=equippable.ArmsEnhancer(),
)

LCap = Item(
    char="C",
    color=(139, 69, 19),
    name="Leather Cap",
    equippable=equippable.LeatherCap(),
)

Bucket = Item(
    char="b",
    color=(139, 69, 19),
    name="Bucket",
    equippable=equippable.Bucket()
)

MShiftHelmet = Item(
    char="C",
    color=(139, 69, 19),
    name= "MakeShift Helmet",
    equippable=equippable.MakeshiftHelmet()
)

MilitaryHelmet = Item(
    char="C",
    color=(139, 69, 19),
    name="Military Helmet",
    equippable=equippable.MilitaryHelmet()
)