#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import random


class World(object):
    def __init__(self, worldfile=None):
        self.savefile = worldfile
        self.chunks = {}

        if self.savefile is not None:
            self.load_world()

    def get_chunk(self, coords):
        # Generate chunk if it doesn't exist
        if coords not in self.chunks:
            print("hi")
            self.generate_chunk(coords)
        return self.chunks[coords]

    def print_chunk(self, chunk):
        for x in chunk:
            for y in x:
                for z in y:
                    print(z, end=" ")
                print()
            print()

    def load_world(self):  # TODO
        self.savefile
        pass

    def save_world(self):
        pass

    def generate_chunk(self, coords, length=16):
        chunk = []
        for x in range(length):
            chunk.append([])
            for y in range(length):
                chunk[x].append([])
                for z in range(length):
                    if random.randint(0, 1) == 0:
                        chunk[x][y].append(0)
                    else:
                        chunk[x][y].append(1)
        self.chunks[coords] = chunk