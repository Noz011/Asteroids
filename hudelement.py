import json
import pygame
import string
import math
from constants import LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

WHITE = (255, 255, 255)



class HudElement():
    """
    1 = PlayerScore
    2 = Timer
    3 = Shape
    """
    def __init__(self, hudElement, x, y, case_inp = 0):
        self.hudElement = hudElement
        self.position = pygame.Vector2(x,y)
        self.case_inp = case_inp


        self.time = 0
        self.text = "0000"
        self.color = "white"
        
        self.lastJson = {"type": "player_hit"}
        self.__score_list= []


    def update(self):
        match(self.case_inp):
            case 0:
                pass
            case 1:
                pass
            case 2:
                self.timeConvertToString()
            case default:
                self.checkShotCollision()
        return
            

    def draw(self, screen):
        if screen == None:
            return
        match(self.case_inp):
            case 0:
                pass
            case 1:
                self.draw_text(screen)
            case 2:
                self.timeConvertToString()
                self.draw_text(screen)
            case 3:
                self.draw_shape(screen)
        

    def timeConvertToString(self):
        self.time = round(pygame.time.get_ticks() // 1000, 0)
        self.text = str(self.time)
    
    def checkShotCollision(self):
        number = int(self.text)

        with open("game_events.jsonl", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if 'asteroid_shot' in line:
                    data = json.loads(line)
                    if data not in self.__score_list:
                        self.__score_list.append(data)
                        number += 1

        self.text = str(number)

    def draw_text(self, screen):
        img = self.hudElement.render(self.text, True, self.color)
        screen.blit(img, (self.position.x, self.position.y))
    
    def draw_shape(self, screen):
        for TRIANGLE in self.hudElement:
            pygame.draw.polygon(screen, WHITE, TRIANGLE, LINE_WIDTH)
        #pygame.draw.polygon(screen, "white", self.hudElement, LINE_WIDTH)