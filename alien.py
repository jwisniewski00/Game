import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """KLasa przedstawiajaca pojedynczego obcego we flocie"""

    def __init__(self, ai_game):
        """Inicjalizacja obcego i zdefiniowanie jego polozenia poczatkowego"""
        super().__init__()
        self.screen = ai_game.screen

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w poblizu lewego gornego rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie dokladnego poziomego polozenia obcego
        self.x = float(self.rect.x)