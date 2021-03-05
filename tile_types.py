from typing import Tuple

import numpy as np

graphics_dt = np.dtype(
    [
        ("ch",np.int32),
        ('fg',"3B"),
        ("bg","3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool),
        ("transparent", np.bool),
        ("dark", graphics_dt),
        ("light", graphics_dt),
    ]
)

def new_tile(
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], tuple[int,int,int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int,int,int]],

) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable,transparent,dark, light), dtype=tile_dt)

SHROUD = np.array((ord(" "),(255,255,255),(0,0,0)), dtype=graphics_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255,255,255), (67,59,173)),
    light=(ord(" "), (255,255,255), (192,199,214)),
)

wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255,255,255), (31,31,31)),
    light=(ord(" "), (255,255,255), (76,79,76)),
)

wall2 = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255,255,255), (222,161,82)),
    light=(ord(" "), (255,255,255), (255,185,95)),
)

floor2 = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (209, 219, 222)),
    light=(ord(" "), (255, 255, 255), (238, 251, 254)),
)

down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), (0, 0, 100), (50, 50, 150)),
    light=(ord(">"), (255, 255, 255), (200, 180, 50)),
)