#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
sys.path.append("prog_utils/")

import pygame
if not pygame.font:
    print("Fehler pygame.font Modul konnte nicht geladen werden!")
if not pygame.mixer:
    print("Fehler pygame.mixer Modul konnte nicht geladen werden!")

import load_files
import display
import world


def mainloop():
    main_config = load_files.Config("config.cfg")
    graphics = main_config.read_section("Graphics")
    a = load_files.Resources()

    pygame.init()
    dimensions = (int(graphics["screen_width"]), int(graphics["screen_height"]))
    screen = pygame.display.set_mode(dimensions)

    pygame.display.set_caption("BloX - L²K")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    clock = pygame.time.Clock()

    running = True
    overworld = world.World()
    overworld.get_chunk((0, 0, 1))

    win = display.Window(screen)
    pos = [-50.0, -200.0, 16.0]
    speed = 2
    while running:
        clock.tick(60)

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key == pygame.K_a:
                    pos[0] -= speed
                elif event.key == pygame.K_d:
                    pos[0] += speed
                elif event.key == pygame.K_w:
                    pos[1] -= speed
                elif event.key == pygame.K_s:
                    pos[1] += speed
                elif event.key == pygame.K_q:
                    pos[2] -= 1
                elif event.key == pygame.K_e:
                    pos[2] += 1

#        dirt = dirt_tile.load_tile()
        win.draw_screen(screen, pos, 64, overworld.get_chunk((0, 0, 0)), 0.25)
        pygame.display.flip()

if __name__ == "__main__":
    mainloop()