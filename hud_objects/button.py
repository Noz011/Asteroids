import pygame
from hud_objects.hudelement import HudElement
from game_objects.shapes.rectangleshape import RectangleShape

class Button(HudElement):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.rectangle_shape = RectangleShape(x, y, width, height)
        self.color = (255, 255, 255)
        self.clicked = False 

    def checkButtonClick(self):
        if self.rectangle_shape.rectangle.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed() == (True, False, False):
                self.clicked = True
            
    def update(self):
        self.checkButtonClick()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle_shape.rectangle)
