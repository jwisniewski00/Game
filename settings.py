class Settings:
    """KLasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicalizacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ustawienia dotyczace statku
        self.sheep_speed = 1.5