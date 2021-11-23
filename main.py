#!F:\Anaconda\envs\hyperenv\python.exe
import pygame
import sys

from pygame import color
from player import Player
from ai import Ai
from settings import Settings
import logging
from math import sqrt

"""
 - black 
 - flake8
 - logging
 - pytest
 - pipenv


"""


class Game:
    """Playground"""

    def __init__(self) -> None:

        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

        self.player = Player(self)
        self.ai = Ai(self, self.player)
        self.settings = Settings()
        self.game_on = True
        self.fps_tick = pygame.time.Clock()
        pygame.font.init()
        dead_message_font = pygame.font.SysFont("sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic", 200)
        self.text_surface = dead_message_font.render("DEAD", True, (255, 30, 70))
        


    def run_game(self):
        """Game loop"""
        while True:
            if self.game_on:
                self.ai.move()
                self._check_ai_los_collision()
                self.player.update()

            self._check_events()
            self._update_screen()
            self.fps_tick.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.fill((200, 200, 200))
        self._check_ai_player_collision()
        self.player.blitme()
        self.ai.draw_me()
        self.ai.show_los()
        self.player.draw_face()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.move_right = True
        elif event.key == pygame.K_LEFT:
            self.player.move_left = True
        elif event.key == pygame.K_UP:
            self.player.move_up = True
        elif event.key == pygame.K_DOWN:
            self.player.move_down = True
        elif event.key == pygame.K_SPACE:
            self.ai.move_random = False
        elif event.key == pygame.K_e:
            self.ai.show_los_boolean = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.move_right = False
        elif event.key == pygame.K_LEFT:
            self.player.move_left = False
        elif event.key == pygame.K_UP:
            self.player.move_up = False
        elif event.key == pygame.K_DOWN:
            self.player.move_down = False
        elif event.key == pygame.K_SPACE:
            self.ai.move_random = True
        elif event.key == pygame.K_e:
            self.ai.show_los_boolean = False

    def _dead_message(self):

        self.screen.blit(self.text_surface, (self.screen.get_rect().centerx - 200, self.screen.get_rect().centery - 200))


    def _check_ai_los_collision(self):
        # use vector to create customized collide with polygon.
        p1 , p2, p3 = self.ai.los_position_tuple
        A = self._get_area()
        B = self._get_area()
        C = self._get_area()
        print(self._get_area(p1,p2,p3))
        if self._get_area(p1,p2,p3) == self.player.rect:
            print("AAAAAAAAAAAAAAAAAAA")


    def _check_ai_player_collision(self):
        if self.player.rect.colliderect(self.ai.rect):
            self._dead_message()
            self.game_on = False

    def _get_area(self, p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return abs((x1 *(y2 - y3) + x2*(y3-y1) + x3*(y1-y2))/2.0)

    def _get_line(self,p1,p2 ):
        return sqrt((p2[0] - p1[0])**2 + (p2[1]-p1[1])**2)


if __name__ == "__main__":

    ai = Game()
    ai.run_game()
