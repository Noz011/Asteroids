import json
import pygame
import string
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
hudElements = []

class Hud():
    def __init__(self):
        self.screenHeight = SCREEN_HEIGHT
        
        

    def append(self, hudElement):
        hudElements.append(hudElement)

    def update(self):
        for hudElement in hudElements:
            hudElement.update()

    def draw(self, screen):
        for hudElement in hudElements:
            hudElement.draw(screen)
    
    

    
