import json
import pygame
import string
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Hud():
    def __init__(self):
        self.screenHeight = SCREEN_HEIGHT
        self.hudElements = []
        

    def append(self, hudElement):
        self.hudElements.append(hudElement)

    def update(self):
        for hudElement in self.hudElements:
            hudElement.update()

    def draw(self, screen):
        for hudElement in self.hudElements:
            hudElement.draw(screen)
    
    

    
