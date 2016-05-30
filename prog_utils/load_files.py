#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from os import listdir
import configparser
import pygame


class Resources(object):
    def __init__(self, path="resources"):
        self.path = path
        print(listdir(self.path))


class Tile(object):
    def __init__(self, filepath, colorkey=None):
        self.filepath = filepath
        self.colorkey = colorkey
        self.image = pygame.image.load(self.filepath)

        if self.image.get_alpha() is None:
            self.image = self.image.convert()
        else:
            self.image = self.image.convert_alpha()

        if self.colorkey is not None:
            if self.colorkey is -1:
                self.colorkey = self.image.get_at((0, 0))
            self.image.set_self.colorkey(self.colorkey, pygame.RLEACCEL)
        self.calc_shadows()

    def calc_shadows(self):
        self.shad_dict = {}
        for shad_level in range(-6, 6):
            top = self.image.copy()
            front = self.image.copy()
            shad_fact_front = round((abs(shad_level) / -6) + 0.875, 3)
            shad_fact_top = round((abs(shad_level) / -6) + 1, 3)
            if 0 < shad_fact_front <= 1:
                arr_front = pygame.surfarray.pixels3d(front)
                arr_front[:, :, :] = arr_front[:, :, :] * shad_fact_front
                del arr_front
            if 0 < shad_fact_top <= 1:
                arr_top = pygame.surfarray.pixels3d(top)
                arr_top[:, :, :] = arr_top[:, :, :] * shad_fact_top
                del arr_top

            if shad_level < 0:
                print(shad_fact_front, 255 * (shad_fact_front - 1))
                front.set_alpha(255 * (1 - shad_fact_front))
                top.set_alpha(255 * (1 - shad_fact_top))

            self.shad_dict[shad_level] = [top, front]
        if self.shad_dict[-4][1] == self.shad_dict[2][1]:
            print("sacre bleu!")


#class for reading a certain section of the cfg-file
#output is a dict
class Config(object):
    def __init__(self, file):
        self.path = file
        self.variables = {}
        self.config = configparser.ConfigParser()
        self.config.read(self.path)

    def read_section(self, section):
        if section in self.config.sections():
            for key in self.config[section]:
                self.variables[key] = self.config.get(section, key)
                if self.variables[key] == -1:
                    raise Warning("No config %s: %s in file %s, skipping"
                          % (section, key, self.path))
        else:
            raise Warning("No such section %s in config %s"
                          % (section, self.path))
        return self.variables