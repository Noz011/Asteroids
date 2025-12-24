import pygame

class HudElement:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        
    def update(self, dt):
        pass

    def draw(self, display):
        pass