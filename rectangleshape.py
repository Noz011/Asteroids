import pygame
import math

class RectangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.dimension = pygame.Vector2(width, height)
        self.velocity = pygame.Vector2(0, 0)

    def collides_with_circle(self, other):
        closest_x = max(self.position.x, min(other.position.x, self.position.x + self.dimension.x))
        closest_y = max(self.position.y, min(other.position.y, self.position.y + self.dimension.y))
        dx = other.position.x - closest_x
        dy = other.position.y - closest_y
        distance = math.sqrt(dx*dx + dy*dy)

        if distance <= other.radius:
            return True
        return False
    
    
    def get_width(self):
        return self.dimension.width
    
    def get_height(self):
        return self.dimension.height

    def update(self,dt):
        self.score.update()

    def draw(self, display):
        pygame.draw.rect(display, "white", self.rectangle)

        
        
        
