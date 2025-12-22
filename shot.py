import pygame
from rectangleshape import RectangleShape
from constants import SHOOT_RADIUS

class Shot(RectangleShape):
    def __init__(self, x, y, height):
        super().__init__(x, y, SHOOT_RADIUS, height)
        self.mask = pygame.mask.from_surface()

    def update(self, dt):
        
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.position.x, self.position.y, self.dimension.x, self.dimension.y))