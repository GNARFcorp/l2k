#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import pygame
import load_files

if not pygame.font:
    print("Fehler pygame.font Modul konnte nicht geladen werden!")
if not pygame.mixer:
    print("Fehler pygame.mixer Modul konnte nicht geladen werden!")


class Window(object):
    def __init__(self, screen, img_format=".png"):
        self.screen = screen
        self.tiles = {}
        tileconfig = load_files.Config("config.cfg")
        tilelist = tileconfig.read_section("Blocks")
        for name in tilelist:
            block_id = int(tilelist[name])
            self.tiles[block_id] = load_files.Tile(name + img_format)

    def draw_tile(self, img_list, coord):
        top = pygame.transform.scale(img_list[0], (self.bl_len, self.bl_len))
        front = pygame.transform.scale(img_list[1], (self.bl_len,
            int(self.bl_len * self.ratio)))
        self.screen.blit(top, coord)
        self.screen.blit(front, (coord[0], coord[1] + self.bl_len))

    def draw_screen(self, screen, pos, pix_per_block, level, ratio=0.25):
        self.ratio = ratio
        self.bl_len = pix_per_block
#        lvl_len = (len(level) - 1,len(level[0]) - 1,len(level[0][0]) - 1)
#        pix_offset = [pos[0] % self.bl_len, pos[1] % self.bl_len]
#        pix_pos = [pos[0] / self.bl_len, pos[1] / self.bl_len, pos[2]]
#        section_x = [x_pos - sight_x, x_pos + sight_x]
#        section_y = [y_pos - sight_y, y_pos + sight_y]
#        section_z = [z_pos, z_pos + sight_z]
        for z, z_level in enumerate(level[::-1]):
            if -4 <= (z - pos[2]) <= 1:
                for y, y_coloumn in enumerate(z_level):
                    for x, block in enumerate(y_coloumn[::-1]):
                        # ID 0 is Air, so nothing will be displayed
                        if block == 0:
                            pass
                        else:
                            coordinate = (x * self.bl_len - pos[0],
                                          (y * self.bl_len - pos[1]) - z * self.ratio * self.bl_len
                                         )
                            self.draw_tile(self.tiles[block].shad_dict[int(-1*(z - pos[2]))], coordinate)