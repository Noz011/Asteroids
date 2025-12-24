import pygame
from game_states.state import State
from game_objects.player import Player
from game_objects.asteroid import Asteroid
from game_objects.asteroidfield import AsteroidField
from game_objects.shot import Shot
from hud_objects.hud import Hud
from bin.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from hud_objects.texthud import TextHud

class GameState(State):
    def __init__(self):

        #Group definitions have to be called before creating Player object
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.events = pygame.sprite.Group()

        Player.containers = (self.updatable, self.drawable, self.events)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.shots, self.updatable, self.drawable)

        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.asteroidField = AsteroidField()

        self.hud = Hud()
        self.hud.append(TextHud((SCREEN_WIDTH/2), 10, ""))
        #self.hud.append(HudElement(pygame.font.Font(None, 30), SCREEN_WIDTH-50, 10, 1))
        self.hud.append(self.player.hudElement)

    def handle_event(self, event):
        self.player.handle_event(event)

    def update(self, dt):
        self.updatable.update(dt)
        self.hud.update()

        for asteroid in self.asteroids:
            if asteroid.collides_with(self.player):
                self.player.hit()
                if self.player.lives <= 0:
                    return "death"

            for shot in self.shots:
                if shot.collides_with_circle(asteroid):
                    asteroid.split()
                    shot.kill()

    def draw(self, screen):
        screen.fill("black")
        self.hud.draw(screen)
        for thing in self.drawable:
            thing.draw(screen)