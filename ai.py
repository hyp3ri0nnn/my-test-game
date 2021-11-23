import pygame
from pygame.sprite import Sprite
import random


class Ai(Sprite):
    def __init__(self, playground, player):
        super().__init__()

        self.playground = playground
        self.screen = playground.screen
        self.screen_rect = playground.screen.get_rect()

        self.rect = pygame.Rect(300, 300, 50, 50)
        # self.rect.top = self.screen_rect.top

        self.player = player
        self.player_rect = player.rect

        self.front = pygame.Rect(330, 330, 30, 30)
        self.move_random = True

        # self.front = "right"

        self.show_los_boolean = False

        self.face = False
        self.last = 0
        self.los_position_tuple = (0,0),(0,0),(0,0)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Create new surface to make transparent obejcts.
        self.test = pygame.Surface((400, 400))
        self.test.set_alpha(0)
        self.test.fill((100, 100, 200))

    def draw_me(self):
        pygame.draw.rect(self.screen, (230, 0, 30), self.rect)
        # pygame.draw.arc(self.screen, (100, 180, 30), self.front, 0.0, 45.0)
        # pygame.draw.ellipse(self.screen, (100, 180, 30), self.front)
        # print(self.rect.topleft)
        self.screen.blit(self.test, (0, 0))

    def show_los(self):
        if self.face:
            if self.face == "right":
                self.position_tuple = (
                    self.rect.midright,
                    (self.rect.centerx + 300, self.rect.centery + 200),
                    (self.rect.centerx + 300, self.rect.centery - 200),
                )

            elif self.face == "left":
                self.position_tuple = (
                    self.rect.midleft,
                    (self.rect.centerx - 300, self.rect.centery + 200),
                    (self.rect.centerx - 300, self.rect.centery - 200),
                )

            elif self.face == "top":
                self.position_tuple = (
                    self.rect.midtop,
                    (self.rect.centerx - 200, self.rect.centery - 300),
                    (self.rect.centerx + 200, self.rect.centery - 300),
                )
            elif self.face == "bottom":
                self.position_tuple = (
                    self.rect.midbottom,
                    (self.rect.centerx - 200, self.rect.centery + 300),
                    (self.rect.centerx + 200, self.rect.centery + 300),
                )
            self.los_position_tuple = self.position_tuple
        
        if self.show_los_boolean:
            pygame.draw.polygon(
                self.screen,
                (180, 160, 50),
                self.position_tuple,
            )

    def move(self):

        directions = ["top", "bottom", "right", "left"]
        direction = random.choice(directions)
        current_time = pygame.time.get_ticks()

        if current_time // 1000 != self.last:

            if self.move_random:

                if direction == "top" and self.rect.top - 100 > 0:
                    self.y -= 100
                    self.face = "top"
                elif (
                    direction == "bottom"
                    and self.rect.bottom + 100 < self.screen_rect.bottom
                ):
                    self.y += 100
                    self.face = "bottom"
                elif (
                    direction == "right"
                    and self.rect.right + 100 < self.screen_rect.right
                ):
                    self.x += 100
                    self.face = "right"
                elif direction == "left" and self.rect.left - 100 > 0:
                    self.x -= 100
                    self.face = "left"

                else:
                    print("unable to path")

            self.last = current_time // 1000

        self.rect.x = self.x
        self.rect.y = self.y
        # pygame.time.wait(100)
