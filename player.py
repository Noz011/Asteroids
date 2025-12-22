import sys
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_GRACE_PERIOD, SCREEN_WIDTH
from shot import Shot
from circleshape import CircleShape
import pygame
from logger import log_state, log_event
from hudelement import HudElement


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.triangles = [(5, 20), (10, 10), (15, 20)], [(25, 20), (30, 10), (35, 20)], [(45, 20), (50, 10), (55, 20)]
        self.hudElement = HudElement(self.triangles, -SCREEN_WIDTH/2, SCREEN_WIDTH-50, 3)
        self.lives = 3
        self.rotation = 0
        self.shot_cooldown = 0
        self.grace_period = PLAYER_GRACE_PERIOD


        self.hudElements = []

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown > 0:
            pass
        else:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot1 = Shot(self.position.x, self.position.y, 10)
            shot_vector = pygame.Vector2(0, 1)
            shot_vector_rotated = shot_vector.rotate(self.rotation)
            shot_vector_rotated_fast = shot_vector_rotated * PLAYER_SHOOT_SPEED
            shot1.velocity = shot_vector_rotated_fast
    
    def hit(self):
        if self.lives <= 0:
            log_event("player_hit")
            print("Game over!")
            sys.exit()
        if self.grace_period <= 0:
            self.lives -= 1
            self.hudElement.hudElement = self.hudElement.hudElement[:-1]
            print(self.hudElement.hudElement)
            print(self.lives)
        self.grace_period = PLAYER_GRACE_PERIOD

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def addHudElement(self, hudElement):
        self.hudElements.append(hudElement)
    
    def update(self, dt):
        self.shot_cooldown -= dt
        self.grace_period -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)