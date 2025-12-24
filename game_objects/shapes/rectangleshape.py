import pygame
import math

class RectangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.rectangle = pygame.Rect(x, y, width, height)
        #self.position = pygame.Vector2(x, y)
        #self.dimension = pygame.Vector2(width, height)
        
        self.velocity = pygame.Vector2(0, 0)

    def collides_with_circle(self, other):
        closest_x = max(self.rectangle.x, min(other.position.x, self.rectangle.x + self.rectangle.width))
        closest_y = max(self.rectangle.y, min(other.position.y, self.rectangle.y + self.rectangle.height))
        dx = other.position.x - closest_x
        dy = other.position.y - closest_y
        distance = math.sqrt(dx*dx + dy*dy)

        if distance <= other.radius:
            return True
        return False

    def update(self,dt):
        pass

    def draw(self, display):
        pass

        
        
        
