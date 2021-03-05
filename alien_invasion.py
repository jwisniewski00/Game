import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry"""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Inwazja obcych')

        self.ship = Ship(self)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()

    def check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # przesuniecie statku w prawa lub lewa strone
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def update_screen(self):
        """Uaktualnianie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
        # Utworzenie egzemplarza gry i jej uruchomienie.
        ai = AlienInvasion()
        ai.run_game()
