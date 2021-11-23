import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, playground) -> None:
        super().__init__()
        self.playground = playground
        self.screen = playground.screen
        self.screen_rect = playground.screen.get_rect()

        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # print(self.rect)
        # self.rect.center = self.screen_rect.

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self._hold_to_move = True

        self.face = False

    def blitme(self):
        pygame.draw.rect(self.screen, (70, 70, 70), self.rect)

    def update(self):
        """Update players location"""

        if self.move_right and (self.rect.right + 100 < self.screen_rect.right):
            self.x += 50
            self.move_right = self._hold_to_move
            self.face = "right"
            # self.rect.clamp_ip(pygame.display.get_surface().get_rect())

        if self.move_left and self.rect.left - 100 > 0:
            self.x -= 50
            self.move_left = self._hold_to_move
            self.face = "left"

        if self.move_up and self.rect.top - 100 > 0:
            self.y -= 50
            self.move_up = self._hold_to_move
            self.face = "top"

        if self.move_down and self.rect.bottom + 100 < self.screen_rect.bottom:
            self.y += 50
            self.move_down = self._hold_to_move
            self.face = "bottom"
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_face(self):
        if self.face:
            if self.face == "right":
                self.los_position_tuple = (
                    self.rect.topright,
                    self.rect.bottomright,
                    (self.rect.centerx + 30, self.rect.centery),
                )

            elif self.face == "left":
                self.los_position_tuple = (
                    self.rect.topleft,
                    self.rect.bottomleft,
                    (self.rect.centerx - 30, self.rect.centery),
                )

            elif self.face == "top":
                self.los_position_tuple = (
                    self.rect.topright,
                    self.rect.topleft,
                    (self.rect.centerx, self.rect.centery - 30),
                )
            elif self.face == "bottom":
                self.los_position_tuple = (
                    self.rect.bottomright,
                    self.rect.bottomleft,
                    (self.rect.centerx, self.rect.centery + 30),
                )
            pygame.draw.polygon(
                self.screen,
                (200, 100, 200),
                self.los_position_tuple,
            )
