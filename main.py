import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from rectangle_hud import RectangleHud
from score import Score


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
    timerScore = Score(SCREEN_WIDTH/2, 10, True)
    pointScore = Score(SCREEN_WIDTH-50, 10)

    dt = 0
    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        timerScore.update()
        pointScore.update()
        timerScore.draw(screen)
        pointScore.draw(screen)

        #Updating the objects and drawing the screen
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
            
        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
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
