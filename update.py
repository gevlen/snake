import pygame
from color import Color
import fonts


class Update:

    def __init__(self):
        self.color = Color()

    def start_game(self, field, text):
        field.start_field.fill((38, 38, 38))
        # field.start_field.blit(pygame.transform.scale(field.game_field_bg, (497, 896)), (783, 0))
        field.start_text.fill([0, 0, 0, 0])
        field.start_button.fill((0, 0, 0, 0))
        field.name_button.fill((0, 0, 0, 0))
        if len(text) == 0:
            field.name_button.set_alpha(102)
            field.name_button.blit(
                fonts.enter_name_font.render('Enter your name', True, pygame.Color('white')), (0, 0))
            pygame.draw.line(field.name_button, (255, 255, 255), (0, 139), (800, 139), 1)
            field.start_text.blit(
                fonts.start_button_font.render('START', True, (255, 255, 255)), (0, 0))
            field.start_button.blit(field.start_text, (220, 31))
        else:
            field.name_button.set_alpha(255)
            field.name_button.blit(
                fonts.name_font.render(text, True, pygame.Color('white')), (0, 0))
            pygame.draw.line(field.name_button, (255, 255, 255), (0, 139), (800, 139), 1)
            field.start_text.blit(
                fonts.start_button_font.render('START', True, (38, 38, 38)), (0, 0))
            field.gradient_for_start_button.blit(field.start_text, (220, 31))
            field.start_button.blit(field.gradient_for_start_button, (0, 0))

        field.start_field.blit(field.snake_title, (433, 114))
        field.start_field.blit(field.start_button, (340, 662))

        field.start_field.blit(field.name_button, (240, 366))

        field.game_field.blit(field.start_field, (0, 0))

    def restart_game(self, field, text):
        field.restart_field.fill((38, 38, 38))
        # field.restart_field.blit(pygame.transform.scale(field.game_field_bg, (497, 896)), (783, 0))
        field.restart_text.fill([0, 0, 0, 0])
        field.restart_button.fill((0, 0, 0, 0))
        field.rename_button.fill((0, 0, 0, 0))
        if len(text) == 0:
            field.rename_button.set_alpha(102)
            field.rename_button.blit(
                fonts.enter_name_font.render('Enter your name', True, pygame.Color('white')), (0, 0))
            pygame.draw.line(field.rename_button, (255, 255, 255), (0, 139), (800, 139), 1)
            field.restart_text.blit(
                fonts.restart_button_font.render('RESTART', True, (255, 255, 255)), (0, 0))
            field.restart_button.blit(field.restart_text, (189, 31))
        else:
            field.rename_button.set_alpha(255)
            field.rename_button.blit(
                fonts.name_font.render(text, True, pygame.Color('white')), (0, 0))
            pygame.draw.line(field.rename_button, (255, 255, 255), (0, 139), (800, 139), 1)
            field.restart_text.blit(
                fonts.restart_button_font.render('RESTART', True, (38, 38, 38)), (0, 0))
            field.gradient_for_restart_button.blit(field.restart_text, (189, 31))
            field.restart_button.blit(field.gradient_for_restart_button, (0, 0))

        field.restart_field.blit(field.restart_button, (340, 662))

        field.restart_field.blit(field.rename_button, (240, 366))
        field.restart_field.blit(field.game_over_image, (253, 114))

        field.game_field.blit(field.restart_field, (0, 0))

    def update_game_window(self, field, settings, new_res):

        field.fake_window.blit(pygame.transform.scale(field.bg, settings.resolution), (0, 0))
        field.fake_window.blit(field.information_field, (640 * 2 + 30 * 2 + 46 * 2, 92 * 2 / 2))
        field.fake_window.blit(field.game_field, (92 * 2 / 2, 92 * 2 / 2))
        field.game_window.blit(pygame.transform.scale(field.fake_window, new_res), (0, 0))

    def update_game_field(self, field, snake, food, frame_counter, score, check_food, ):
        [pygame.draw.rect(field.fake_game_field, (133, 133, 133), i_rect, 1) for i_rect in field.grid]
        field.game_field.fill((38, 38, 38))

        field.game_field.blit(field.fake_game_field, (0, 0))
        snake.draw_snake(field.game_field, frame_counter)
        check_food()
        food.draw_food(field.game_field)

    def update_information_field(self, field, score):
        # information_field
        field.information_field.fill([0, 0, 0, 0])

        # score field
        field.score_field.fill(self.color.score_field_fill)
        field.score_title_field.fill((0, 0, 0, 0))
        field.score_field.blit(field.score_image, (120, 0))
        field.score_title_field.blit(
            fonts.score_title_font.render('Score:', True, (255, 255, 255)), (0, 0))
        field.score_field.blit(field.score_title_field, (20, 20))
        field.score_field.blit(
            fonts.score_font.render(str(score.score), True, self.color.score_field_score), (20, 104))
        field.information_field.blit(field.score_field, (0, 0))

        # records field
        field.records_field.fill((38, 38, 38))
        field.record_title_field.fill((0, 0, 0, 0))
        field.record_title_field.blit(
            fonts.record_title_font.render('Records:', True, (255, 255, 255)), (0, 0))
        field.records_field.blit(field.record_title_field, (20, 20))

        y = 120
        y1 = 140
        for x in range(3):
            score_text = fonts.record_score_font.render(str(score.record[x][1]), True, (255, 255, 255))
            pygame.draw.circle(field.records_field, self.color.leaders[x], (30, y1), 7)
            field.records_field.blit(
                fonts.record_name_font.render(score.record[x][0], True, (255, 255, 255)), (45, y))
            field.records_field.blit(score_text, (396 - 20 - score_text.get_rect().size[0], y))
            y += 40
            y1 += 40

        field.record_not_leaders_field.fill((0, 0, 0, 0))
        y = 0
        for x in range(3, len(score.record)):
            score_text = fonts.record_score_font.render(str(score.record[x][1]), True, (255, 255, 255))
            field.record_not_leaders_field.blit(
                fonts.record_name_font.render(score.record[x][0], True, (255, 255, 255)), (20, y))
            field.record_not_leaders_field.blit(score_text, (396 - 20 - score_text.get_rect().size[0], y))

            y += 40
        field.records_field.blit(field.record_not_leaders_field, (0, 240))

        field.information_field.blit(field.records_field, (0, 242))
