import pygame
from game_objects.shapes.rectangleshape import RectangleShape
from bin.constants import SHOOT_RADIUS

class Shot(RectangleShape):
    def __init__(self, x, y, height):
        super().__init__(x, y, SHOOT_RADIUS, height)

        self.base_surface = pygame.Surface((self.rectangle.width, self.rectangle.height), pygame.SRCALPHA)
        self.base_surface.fill((255,255,255))
        
        self.surface = self.base_surface
        self.mask = pygame.mask.from_surface(self.surface)
        
    def rotate_bullet(self, player_rotation):
        #rotate Rectangle to Player rotation
        old_center = self.rectangle.center

        self.surface = pygame.transform.rotate(self.base_surface, -player_rotation)

        #update rect from rotated surface
        self.rectangle = self.surface.get_rect(center=old_center)

        #rebuild mask
        self.mask = pygame.mask.from_surface(self.surface)

    def update(self, dt):
        position = pygame.Vector2(self.rectangle.x, self.rectangle.y)
        position += self.velocity * dt
        self.rectangle.x = position.x
        self.rectangle.y = position.y
        

    def draw(self, screen):
        screen.blit(self.surface, self.rectangle)
