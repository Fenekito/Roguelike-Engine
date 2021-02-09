from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="UNSC MARINE",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

grunt = Actor(
    char="G",
    color=(255, 65, 7),
    name="Melee Grunt",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=1, power=3)
    )
elite = Actor(
    char="E",
    color=(78, 81, 255),
    name="Melee Elite",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=33, defense=4, power=8)
)
jackal = Actor(
    char="J",
    color=(78, 81, 255),
    name="Melee Skyrmisher",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=15, defense=2, power=4)
)