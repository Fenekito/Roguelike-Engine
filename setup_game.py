"""Handle the loading and initialization of game sessions."""
from __future__ import annotations

import copy
from typing import Optional

import tcod

import copy
import lzma
import pickle
import traceback
import color
from engine import Engine
import entities_factory
import input_handlers
from game_map import GameWorld
from pygame import mixer

# Load the background image and remove the alpha channel.
background_image = tcod.image.load("menu_background.png")[:, :, :3]


def new_game() -> Engine:
    """Return a brand new game session as an Engine instance."""
    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    player = copy.deepcopy(entities_factory.player)

    engine = Engine(player=player)

    engine.game_world = GameWorld(
        engine=engine,
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
    )
    engine.game_world.generate_floor()
    engine.update_fov()

    engine.message_log.add_message(
        "The World is not the same anymore... Have a good death friend.", color.welcome_text
    )

    rknife = copy.deepcopy(entities_factory.rknife)
    LJacket = copy.deepcopy(entities_factory.LJacket)

    rknife.parent = player.inventory
    LJacket.parent = player.inventory

    player.inventory.items.append(rknife)
    player.equipment.toggle_equip(rknife, add_message=False)

    player.inventory.items.append(LJacket)
    player.equipment.toggle_equip(LJacket, add_message=False)

    return engine

def load_game(filename: str) -> Engine:
    """Load an Engine instance from a file."""
    with open(filename, "rb") as f:
        engine = pickle.loads(lzma.decompress(f.read()))

    mixer.music.load('Desolate Hallways.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)
    assert isinstance(engine, Engine)
    return engine

class MainMenu(input_handlers.BaseEventHandler):
    """Handle the main menu rendering and input."""

    def on_render(self, console: tcod.Console) -> None:
        """Render the main menu on a background image."""
        console.draw_semigraphics(background_image, 0, 0)

        console.print(
            console.width // 2,
            console.height // 2 - 4,
            "Under Desolation",
            fg=color.menu_title,
            alignment=tcod.CENTER,
        )
        console.print(
            console.width // 2,
            console.height - 2,
            "By Fenekito",
            fg=color.menu_title,
            alignment=tcod.CENTER,
        )

        menu_width = 24
        for i, text in enumerate(
            ["[N]ew game", "[C]ontinue", "[Q]uit"]
        ):
            console.print(
                console.width // 2,
                console.height // 2 - 2 + i,
                text.ljust(menu_width),
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.CENTER,
                bg_blend=tcod.BKGND_ALPHA(64),
            )

    def ev_keydown(
        self, event: tcod.event.KeyDown
    ) -> Optional[input_handlers.BaseEventHandler]:
        if event.sym in (tcod.event.K_q, tcod.event.K_ESCAPE):
            raise SystemExit()
        elif event.sym == tcod.event.K_c:
            try:
                return input_handlers.MainGameEventHandler(load_game("savegame.udsav"))
            except FileNotFoundError:
                return input_handlers.PopupMessage(self, "No saved game to load.")
            except Exception as exc:
                traceback.print_exc()  # Print to stderr.
                return input_handlers.PopupMessage(self, f"Failed to load save:\n{exc}")
        elif event.sym == tcod.event.K_n:
            mixer.music.load('Desolate Hallways.mp3')
            mixer.music.set_volume(0.3)
            mixer.music.play(-1)
            return input_handlers.MainGameEventHandler(new_game())

        return None
