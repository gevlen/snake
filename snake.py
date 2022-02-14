import pygame
from copy import deepcopy



class Snake:
    def __init__(self, field, settings, color):
        self.settings = settings
        self.color = color

        self.dx = 0
        self.dy = 0
        self.head = pygame.Rect(field.get_rect().center[0] + 1, field.get_rect().center[1] + 1,
                                self.settings.small_tile_w,
                                self.settings.small_tile_h)
        self.tale = [
            pygame.Rect((field.get_rect().center[0] + self.settings.tile_w * x) + 1, field.get_rect().center[1] + 1,
                        self.settings.small_tile_w,
                        self.settings.small_tile_h) for x
            in range(1, 3)]

        self.snake_speed = self.settings.speed
        self.flag = True

    def move_x(self, dx):
        self.dx += dx
        self.dy = 0

    def move_y(self, dy):
        self.dy += dy
        self.dx = 0

    def add_tale(self):
        self.food_for_tale = pygame.Rect(self.tale[len(self.tale) - 1].x, self.tale[len(self.tale) - 1].y,
                                         self.settings.small_tile_w, self.settings.small_tile_h)
        self.tale.append(self.food_for_tale)

    def draw_snake(self, surface, frame):
        self.old_tail = deepcopy(self.tale)
        self.old_head = deepcopy(self.head)
        if frame % self.snake_speed == 0:
            self.head.y += self.dy
            self.head.x += self.dx
            self.flag = True

        pygame.draw.rect(surface, self.color.snake, self.head)
        for i in range(len(self.tale)):
            if self.head == self.old_head:
                pygame.draw.rect(surface, self.color.snake, self.tale[i])
            else:
                if i == 0:
                    self.tale[i].x = self.old_head.x
                    self.tale[i].y = self.old_head.y
                    pygame.draw.rect(surface, self.color.snake, self.tale[i])
                else:
                    self.tale[i].x = self.old_tail[i - 1].x
                    self.tale[i].y = self.old_tail[i - 1].y
                    pygame.draw.rect(surface, self.color.snake, self.tale[i])

    def restart(self, field):
        self.dx = 0
        self.dy = 0
        self.head = pygame.Rect(field.get_rect().center[0] + 1, field.get_rect().center[1] + 1,
                                self.settings.small_tile_w,
                                self.settings.small_tile_h)
        self.tale = [
            pygame.Rect((field.get_rect().center[0] + self.settings.tile_w * x) + 1, field.get_rect().center[1] + 1,
                        self.settings.small_tile_w,
                        self.settings.small_tile_h) for x
            in range(1, 3)]

        self.snake_speed = self.settings.speed
        self.flag = True

