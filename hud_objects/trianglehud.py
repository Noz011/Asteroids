import pygame
from bin.constants import LINE_WIDTH
from hud_objects.hudelement import HudElement
from game_objects.shapes.triangleshape import TriangleShape

class TriangleHud(HudElement):
    def __init__(self, triangles, x, y):
        super(). __init__(x, y)

        self.triangles = triangles
        self.color = "white"
        
    def update(self):
        pass
    
    def draw(self, screen):
        for triangle in self.triangles:
            pygame.draw.polygon(screen, self.color, triangle, LINE_WIDTH)