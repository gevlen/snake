import pygame


class Control:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.start = True
        self.restart = False
        self.need_input = True
        self.name_view = False

    def control_keyboard(self, event, snake, settings):

        if event.key == pygame.K_LEFT:
            if self.dx == 0 and snake.flag:
                self.dy = 0
                self.dx = -settings.tile_w
                snake.move_x(self.dx)
                snake.flag = False

        elif event.key == pygame.K_RIGHT:
            if self.dx == 0 and self.dy == 0:  # при старте не пойдет через чебя
                pass
            elif self.dx == 0 and snake.flag:
                self.dy = 0
                self.dx = settings.tile_w
                snake.move_x(self.dx)
                snake.flag = False

        elif event.key == pygame.K_DOWN:
            if self.dy == 0 and snake.flag:
                self.dx = 0
                self.dy = settings.tile_h
                snake.move_y(self.dy)
                snake.flag = False

        elif event.key == pygame.K_UP:
            if self.dy == 0 and snake.flag:
                self.dx = 0
                self.dy = -settings.tile_h
                snake.move_y(self.dy)
                snake.flag = False
        elif event.key == pygame.K_SPACE:
            self.old_speed = settings.speed
            settings.speed = 1

    def control_mouse(self, event, field, input_text, coef):
        if 432 * coef[0] < event.pos[0] < (432 + field.start_button.get_size()[0]) * coef[0] and 754 * coef[1] < \
                event.pos[1] < (754 + field.start_button.get_size()[1]) * coef[1]:
            if input_text != '':
                self.need_input = False
                self.start = False
                self.name_view = True

        if 432 * coef[0] < event.pos[0] < (432 + field.restart_button.get_size()[0]) * coef[0] and 754 * coef[1] < \
                event.pos[1] < (754 + field.restart_button.get_size()[1]) * coef[1]:
            if input_text != '':
                self.need_input = False
                self.start = False
                self.restart = False
                self.name_view = True

    def control_for_text(self, event, input_text):
        if self.need_input:
            if event.key == pygame.K_RETURN:
                if input_text != '':
                    if self.start == True:
                        self.start = False
                        return input_text
                    else:
                        self.restart = False
                        return input_text
                else:
                    input_text += ''
                    return input_text
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
                return input_text
            else:
                if len(input_text) < 11:
                    input_text += event.unicode
                return input_text

    def restart_control(self):
        self.dx = 0
        self.dy = 0
        self.start = False
        self.restart = True
        self.need_input = True
        self.name_view = False
