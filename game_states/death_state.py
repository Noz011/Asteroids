import pygame
from bin.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_states.state import State
from hud_objects.hud import Hud
from hud_objects.button import Button
from hud_objects.texthud import TextHud

class DeathState(State):
    def __init__(self):
        self.hud = Hud()
        self.hud.append(TextHud(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "You Died"))
        self.hud.append(Button(0, 300, SCREEN_WIDTH/2, 100))
        self.hud.append(Button(0, 500, SCREEN_WIDTH/2, 100))

    def handle_events(self):
        pass

    def update(self, dt):
        self.hud.update()
        if self.hud.hudElements[0].clicked:
            return "game"

    def draw(self, screen):
        self.hud.draw(screen)