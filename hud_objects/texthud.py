import pygame
from hud_objects.hudelement import HudElement

class TextHud(HudElement):
    def __init__(self, x, y, text):
        super().__init__(x, y)
        self.font = pygame.font.Font(None, 30)
        self.text = text
        self.color = (255, 255, 255)
        self.text = "0000"
        self.clicked = False
    
    def timeConvertToString(self):
        self.time = round(pygame.time.get_ticks() // 1000, 0)
        self.text = str(self.time)


    def update(self):
        self.timeConvertToString()

    def draw(self, screen):
        img = self.font.render(self.text, True, self.color)
        