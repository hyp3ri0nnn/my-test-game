import pygame
from pygame.sprite import Sprite
import random 

class Ai(Sprite):

    def __init__(self, playground):
        super().__init__()

        self.playground = playground
        self.screen = playground.screen 
        self.screen_rect = playground.screen.get_rect()

        self.rect = pygame.Rect(300,300,50,50)
        # self.rect.top = self.screen_rect.top

        self.move_random = True

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_me(self):
        pygame.draw.rect(self.screen, (230, 0, 30), self.rect)


    # def move(self):
    #     random_path = [100]
    #     directions =  [self.x, self.y]
    #     indexes = [0, 1]
    #     if self.move_random and \
    #         (self.rect.top - 100 > 0) and \
    #             (self.rect.right + 100 < self.screen_rect.right) and \
    #                 (self.rect.bottom + 100 < self.screen_rect.bottom) and \
    #                     (self.rect.left - 100 > 0 ):

    #         # index = random.choice(indexes)
    #         print(directions)
    #         directions[0] += random.choice(random_path)
            
    #         # print(index)
    #         print(directions[0])
    #         print(directions)
    #         # other_index = 0 if index == 1 else 1
    #         # directions[index] = direction
    #         # directions[other_index] = directions[other_index]

    def move(self):

        directions = ["top", "bottom", "right", "left"]
        direction = random.choice(directions)

        if self.move_random:

            if direction == "top" and self.rect.top - 100 > 0:
                self.y -= 100
            elif direction == "bottom" and self.rect.bottom + 100 < self.screen_rect.bottom:
                self.y += 100
            elif direction == "right" and self.rect.right + 100 < self.screen_rect.right:
                self.x += 100
            elif direction == "left" and self.rect.left - 100 > 0:
                self.x -= 100
            
            else:
                print("unable to path")


        self.rect.x = self.x
        self.rect.y = self.y
        pygame.time.wait(1000)
