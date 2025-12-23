import pygame
from game_states.state import State
from hud_objects.hud import Hud
from hud_objects.hudelement import HudElement
from bin.constants import SCREEN_WIDTH

class MenuState(State):
    def __init__(self):
        self.hud = Hud()
        self.hud.append(HudElement(pygame.Rect(0, 100, SCREEN_WIDTH/2, 100), 200,200, 4))
        self.hud.append(HudElement(pygame.Rect(0, 300, SCREEN_WIDTH/2, 100), 200,200, 4))
        self.hud.append(HudElement(pygame.Rect(0, 500, SCREEN_WIDTH/2, 100), 200,200, 4))
        
    def handle_event(self, event):
        pass
    
    def update(self, dt):
        self.hud.update()
        if self.hud.hudElements[0].clicked:
            return "game"
        
    def draw(self, screen):
        screen.fill("grey")
        self.hud.draw(screen)