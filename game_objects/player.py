import sys
from bin.constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_GRACE_PERIOD, SCREEN_WIDTH
from game_objects.shot import Shot
from game_objects.shapes.circleshape import CircleShape
import pygame
from bin.logger import log_state, log_event
from hud_objects.trianglehud import TriangleHud


class Player(CircleShape):
    INVULN_EVENT = pygame.USEREVENT + 1
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.triangles = [(5, 20), (10, 10), (15, 20)], [(25, 20), (30, 10), (35, 20)], [(45, 20), (50, 10), (55, 20)]
        self.hudElement = TriangleHud(self.triangles, -SCREEN_WIDTH/2, SCREEN_WIDTH-50)
        self.lives = 3
        self.rotation = 0
        self.shot_cooldown = 0
        self.grace_period = PLAYER_GRACE_PERIOD

        self.visable = True
        self.hudElements = []

    # in the Player class
    def handle_event(self, event):
        if event.type == self.INVULN_EVENT:
            self.visable = not self.visable

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

            shot1.rotate_bullet(self.rotation)

            shot_vector = pygame.Vector2(0, 1)
            shot_vector_rotated = shot_vector.rotate(self.rotation)
            shot_vector_rotated_fast = shot_vector_rotated * PLAYER_SHOOT_SPEED
            shot1.velocity = shot_vector_rotated_fast

    
    
    def hit(self):
        if self.lives <= 0:
            log_event("player_hit")
            print("Game over!")


        if self.grace_period <= 0:
            self.lives -= 1
            self.hudElement = self.hudElement.triangles[:-1]

            pygame.time.set_timer(self.INVULN_EVENT, 200)
        
        self.grace_period = PLAYER_GRACE_PERIOD




    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def addHudElement(self, hudElement):
        self.hudElements.append(hudElement)
    

    def update(self, dt):
        self.shot_cooldown -= dt
        self.grace_period -= dt
        if self.grace_period <= 0:
            pygame.time.set_timer(self.INVULN_EVENT, 0)
            self.visable = True
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
        color = ""
        if self.visable:
            color = "white"
        else:
            color = "black"
    
        pygame.draw.polygon(screen, color, self.triangle(), LINE_WIDTH)