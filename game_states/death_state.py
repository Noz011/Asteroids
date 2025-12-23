import pygame
from bin.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_states.state import State
from hud_objects.hud import Hud
from hud_objects.hudelement import HudElement

class DeathState(State):
    def __init__(self):
        self.hud = Hud()
        self.hud.append(HudElement(pygame.font.Font(None, 100), SCREEN_WIDTH/2, SCREEN_HEIGHT/2,1))
        self.hud.append(HudElement(pygame.Rect(0, 300, SCREEN_WIDTH/2, 100), 200,200, 4))
        self.hud.append(HudElement(pygame.Rect(0, 500, SCREEN_WIDTH/2, 100), 200,200, 4))

    def handle_events(self):
        pass

    def update(self, dt):
        self.hud.update()
        if self.hud.hudElements[0].clicked:
            return "game"

    def draw(self, screen):
        self.hud.draw(screen)