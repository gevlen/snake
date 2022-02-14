from random import randrange
import pygame



class Food:
    def __init__(self, settings, color):
        self.settings = settings
        self.color = color
        self.set_current_food()

    def set_current_food(self):
        self.x = randrange(self.settings.w1)
        self.y = randrange(self.settings.h1)
        self.current_food = pygame.Rect((self.settings.tile_w * self.x) + 1, (self.settings.tile_h * self.y) + 1,
                                        self.settings.small_tile_w, self.settings.small_tile_h)


    def draw_food(self, surface):
        pygame.draw.rect(surface, self.color.food, self.current_food)

    def restart(self):
        self.set_current_food()

