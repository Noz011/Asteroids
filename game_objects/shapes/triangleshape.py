import pygame
import math

from bin.constants import LINE_WIDTH, PLAYER_TURN_SPEED

class TriangleShape(pygame.sprite.Sprite):
    def __init__(self, base_length, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.base_length = base_length
        self.height = height
        self.color = "white"
        


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        c = self.base_length
        a = math.sqrt((self.base_length*0.5)^2 + self.height^2)
        b = a       
        return [a, b, c]
    
    def rotate(self, dt):   
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self):
        pass

    def draw(self, screen):
        pass