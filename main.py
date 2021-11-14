#!F:\Anaconda\envs\hyperenv\python.exe
import pygame 
import sys
from player import Player
from ai import Ai

class Game:
    """Playground"""
    def __init__(self) -> None:
        
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

        self.player = Player(self)
        self.ai = Ai(self)

        
    def run_game(self):
        """Game loop"""
        while True:
            self._check_events()
            self.player.update()
            self.ai.move()
            self._update_screen()


    def _update_screen(self):
        self.screen.fill((200, 200, 200))
        self.player.blitme()
        self.ai.draw_me()
        
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

if __name__ == "__main__":

    ai = Game()
    ai.run_game()