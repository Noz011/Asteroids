import pygame
from hud import Hud

class RectangleHud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.rectangle = pygame.rect.RectType(x, y)
        self.score = Hud()
        
    def update(self,dt):
        self.score.update()

        

    def draw(self, display):
        pygame.draw.rect(display, "white", self.rectangle)
        self.score.draw_text(display,"white", )
        
        
        
