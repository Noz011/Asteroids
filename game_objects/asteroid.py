import pygame
import random
from game_objects.shapes.circleshape import CircleShape
from bin.logger import log_event
from bin.constants import LINE_WIDTH , ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        self.mask = pygame.mask.from_surface(self.surface)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rotation_one = self.velocity.rotate(random.uniform(20, 50))
        rotation_two = self.velocity.rotate(-random.uniform(20, 50))
        radius_new = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid_two = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid_one.velocity = rotation_one * 1.2
        asteroid_two.velocity = rotation_two * 1.2


    def update(self, dt):
        unit_vector = pygame.Vector2(0, -1)
        down_vector = self.velocity * dt
        self.position +=  down_vector

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH) 
