import pygame
import sys
from bin.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from bin.logger import log_state, log_event
from game_objects.player import Player
from game_objects.asteroid import Asteroid
from game_objects.asteroidfield import AsteroidField
from game_objects.shot import Shot
from hud_objects.hud import Hud
from hud_objects.hudelement import HudElement


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Group definitions have to be called before creating Player object
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    events = pygame.sprite.Group()
    #rectangle_hud = pygame.sprite.Group()
    
    play = False

    Player.containers = (updatable, drawable, events)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    #Creating objects
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    #initialising Pygame
    pygame.init()

    #Setting screen resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Hud
    hud_main_menu = Hud()
    hud_main_menu.append(HudElement(pygame.Rect(0, 100, SCREEN_WIDTH/2, 100), 200,200, 4))
    hud_main_menu.append(HudElement(pygame.Rect(0, 300, SCREEN_WIDTH/2, 100), 200,200, 4))
    hud_main_menu.append(HudElement(pygame.Rect(0, 500, SCREEN_WIDTH/2, 100), 200,200, 4))

    hud_game = Hud()
    hud_game.append(HudElement(pygame.font.Font(None, 30),(SCREEN_WIDTH/2), 10, 2))
    hud_game.append(HudElement(pygame.font.Font(None, 30), SCREEN_WIDTH-50, 10, 1))
    hud_game.append(player1.hudElement)

    STATE_MENU = "menu"
    STATE_GAME = "game"

    state = STATE_MENU
    running = True

    #Creating Clock object
    clock = pygame.time.Clock()

    while(running):
        dt = clock.tick(60)
        

        if state == STATE_MENU:
            draw_menu()
        elif state == STATE_GAME:
            draw_game()

def draw_menu():
    pass

def draw_game():
    pass


