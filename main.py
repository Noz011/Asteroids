import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from rectangle_hud import RectangleHud
from hud import Hud
from hudelement import HudElement

TRIANGLES = [(5, 20), (10, 10), (15, 20)], [(25, 20), (30, 10), (35, 20)], [(45, 20), (50, 10), (55, 20)]

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Group definitions have to be called before creating Player object
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #rectangle_hud = pygame.sprite.Group()
    


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    #RectangleHud.containers = (updatable, drawable)
    #Creating objects
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()
    #initialising Pygame
    pygame.init()
    #Setting screen resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Creating Clock object
    clock = pygame.time.Clock()

    #Hud
    hud = Hud()
    h1 = HudElement(pygame.font.Font(None, 30),(SCREEN_WIDTH/2), 10, 2)
    h2 = HudElement(pygame.font.Font(None, 30), SCREEN_WIDTH-50, 10, 1)
    h3 = HudElement(TRIANGLES,-SCREEN_WIDTH/2, SCREEN_WIDTH-50, 3)
    hud.append(h1)
    hud.append(h2)
    hud.append(h3)

    player1.addHudElement(h3)

    #playerLives = Hud(10, 10)

    dt = 0
    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        hud.update()
        hud.draw(screen)
        
        #Updating the objects and drawing the screen
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
            
        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                player1.hit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        

        pygame.display.flip()
        #setting Framerate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
