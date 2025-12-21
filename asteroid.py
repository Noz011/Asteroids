import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    
    def update(self, dt):
        unit_vector = pygame.Vector2(0, -1)
        down_vector = self.velocity * dt
        self.position +=  down_vector

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH) 
