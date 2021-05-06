#!/bin/python3
import sys
from pyanvil import World, BlockState, Material
# from pyanvil import world
import random

import numpy as np

with World('Flat', save_location='C:/Users/gsmel/AppData/Roaming/.minecraft/saves', debug=True) as wrld:
    cv = wrld.get_canvas()
    # cv.select_rectangle((10, 10, 10), (15, 15, 15)).fill(BlockState(Material.diamond_block, {}))

    # cv.select_rectangle((-100, 4, -100), (100, 15, 100)).fill(BlockState(Material.air, {}))
    # cv.select_rectangle((-1, 4, -1), (1, 48, 1)).fill(BlockState(Material.diamond_block, {}))
    # cv.select_rectangle((-100, 3, -100), (100, 3, 100)).fill(BlockState(Material.grass_block, {}))



    # path = []
    # loc = (0, 0)
    # dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # direction = 0
    # for step in range(500):
    #     path.append((loc[0], 4, loc[1]))
    #     loc = tuple(map(lambda a, b: a + b, loc, dirs[direction]))
        
    #     if random.randrange(100) % 20 == 0:
    #         # print("test")
    #         direction = (direction + 1) % len(dirs)

    
    # for block in path:
    #     # cv.select_rectangle(block, block).fill(BlockState(Material.obsidian, {}))
    #     print(block)
    #     myBlock = wrld.get_block(block)
    #     myBlock.set_state(BlockState(Material.obsidian, {}))

    


print("Saved!")