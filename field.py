import pygame
import gradients


class Game_fields:
    def __init__(self, settings):
        self.settings = settings
        self.game_window = pygame.display.set_mode(self.settings.resolution, pygame.RESIZABLE)

        self.game_field_bg = pygame.image.load('images/game_field_image.png').convert_alpha()

        self.start_field = pygame.Surface(self.settings.start_field_size, pygame.SRCALPHA)
        self.snake_title = pygame.image.load('images/snake.png').convert_alpha()
        self.game_over_image = pygame.image.load('images/game_over.png').convert_alpha()
        self.start_button = pygame.Surface((600, 120), pygame.SRCALPHA)
        self.gradient_for_start_button = gradients.horizontal(self.start_button.get_size(), (144, 215, 245, 255), (188, 144, 245, 255))
        self.start_text = pygame.Surface((159, 58), pygame.SRCALPHA)
        self.start_text.set_alpha(25)
        self.name_button = pygame.Surface((800, 140), pygame.SRCALPHA)


        self.restart_field = pygame.Surface(self.settings.start_field_size)
        self.restart_button = pygame.Surface((600, 120), pygame.SRCALPHA)
        self.gradient_for_restart_button = gradients.horizontal(self.restart_button.get_size(), (144, 215, 245, 255),
                                                              (188, 144, 245, 255))
        self.restart_text = pygame.Surface((220, 58), pygame.SRCALPHA)
        self.restart_text.set_alpha(25)
        self.rename_button = pygame.Surface((800, 140), pygame.SRCALPHA)

        self.game_field = pygame.Surface(self.settings.field_size,pygame.SRCALPHA)
        self.fake_game_field = pygame.Surface(self.settings.field_size, pygame.SRCALPHA).convert_alpha()
        self.fake_game_field.set_alpha(50)

        self.bg = pygame.image.load('images/Background.png').convert_alpha()  # convert()
        self.fake_window = self.game_window.copy()

        self.information_field = pygame.Surface(self.settings.information_field_size, pygame.SRCALPHA)

        self.score_field = pygame.Surface(self.settings.score_field_size)
        self.score_title_field = pygame.Surface((149, 59), pygame.SRCALPHA)
        self.score_title_field.set_alpha(102)
        self.score_image = pygame.image.load('images/snake_score.png').convert_alpha()


        self.records_field = pygame.Surface(self.settings.records_field_size)
        self.record_title_field = pygame.Surface((205, 59), pygame.SRCALPHA)
        self.record_title_field.set_alpha(102)
        self.record_not_leaders_field = pygame.Surface((396, 414), pygame.SRCALPHA)
        self.record_not_leaders_field.set_alpha(102)

        self.game_over_field = pygame.Surface(self.settings.game_over_field_size)

        self.left_border = 0
        self.right_border = self.game_field.get_rect().width
        self.up_border = 0
        self.down_border = self.game_field.get_rect().height

        pygame.display.set_caption("Snake")

        self.grid = [
            pygame.Rect(x * self.settings.tile_w, y * self.settings.tile_h, self.settings.tile_w, self.settings.tile_h)
            for x in range(self.settings.w1) for y in range(self.settings.h1)]
