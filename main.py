import sys
import pygame
from field import Game_fields
from snake import Snake
from food import Food
from settings import Settings
from score import Score
from update import Update
from control import Control
from color import Color


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.color = Color()
        self.field = Game_fields(self.settings)
        self.control = Control()
        self.food = Food(self.settings, self.color)
        self.score = Score()
        self.update = Update()

        self.snake = Snake(self.field.game_field, self.settings, self.color)
        self.clock = pygame.time.Clock()
        self.loop = True

        self.frame_counter = 0
        self.new_res = self.settings.resolution

        self.input_text = ''
        self.need_input = True
        self.coef = [1, 1]

    def restart(self):
        self.control.restart_control()

        self.food.restart()
        self.score.restart()
        self.snake.restart(self.field.game_field)
        self.frame_counter = 0

    def game_difficult(self):
        if not len(self.snake.tale) % 6:
            if not self.snake.snake_speed == 1:
                self.snake.snake_speed -= 1
            self.score.score_increase += 50

    def check_food_appear(self):
        if pygame.Rect.colliderect(self.snake.head, self.food.current_food):
            return True
        for i in range(len(self.snake.tale)):
            if pygame.Rect.colliderect(self.snake.tale[i], self.food.current_food):
                return True

    def check_food(self):
        if pygame.Rect.colliderect(self.snake.head, self.food.current_food):
            self.game_difficult()
            self.score.score = self.score.set_current_score(self.score.score_increase)
            self.snake.add_tale()
            self.food.set_current_food()
            while self.check_food_appear():
                self.food.set_current_food()

    def check_game_over(self):
        for i in range(1, len(self.snake.tale)):
            if pygame.Rect.colliderect(self.snake.head, self.snake.tale[i]):
                return True
        if self.snake.head.x < self.field.left_border or self.snake.head.x > self.field.right_border:
            return True
        elif self.snake.head.y < self.field.up_border or self.snake.head.y > self.field.down_border:
            return True
        return False

    def update_when_start(self):
        self.update.start_game(self.field, self.input_text)
        self.update.update_information_field(self.field, self.score)
        self.update.update_game_window(self.field, self.settings, self.new_res)

    def update_when_restart(self):
        self.update.restart_game(self.field, self.input_text)
        self.update.update_information_field(self.field, self.score)
        self.update.update_game_window(self.field, self.settings, self.new_res)

    def update_while_play(self):
        self.update.update_game_field(self.field, self.snake, self.food, self.frame_counter, self.score,
                                      self.check_food)
        self.update.update_information_field(self.field, self.score)
        self.update.update_game_window(self.field, self.settings, self.new_res)

        if self.check_game_over():
            if not self.score.score == 0:
                self.score.set_record(self.input_text)
            self.restart()

    def game_loop(self):
        while self.loop:
            self.clock.tick(self.settings.fps)
            self.frame_counter += 1
            self.record = self.score.record

            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    self.field.game_window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                    self.new_res = event.size
                    self.coef[0] = self.new_res[0] / self.settings.resolution[0]
                    self.coef[1] = self.new_res[1] / self.settings.resolution[1]
                elif event.type == pygame.QUIT:
                    if not self.score.score == 0:
                        self.score.set_record(self.input_text)
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.control.control_keyboard(event, self.snake, self.settings)
                    if self.control.need_input:
                        self.input_text = self.control.control_for_text(event, self.input_text)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.control.control_mouse(event, self.field, self.input_text, self.coef)

            if self.control.start:
                self.update_when_start()
            elif self.control.restart:
                self.update_when_restart()
            else:
                if len(self.snake.tale) == 2:
                    self.score.start_play()
                self.update_while_play()
            pygame.display.update()


if __name__ == '__main__':
    # создание экземпляра и запуск игры
    p = Game()
    p.game_loop()
