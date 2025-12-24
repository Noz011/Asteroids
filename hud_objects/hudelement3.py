import json
import pygame
import string
import math
from bin.constants import LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

WHITE = (255, 255, 255)



class HudElement():
    """
    1 = PlayerScore
    2 = Timer
    3 = Triangle
    4 = Rectangle
    """
    def __init__(self, hudElement, x, y, case_inp = 0):
        self.hudElement = hudElement
        self.position = pygame.Vector2(x,y)
        self.case_inp = case_inp
        self.clicked = False


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
                self.checkShotCollision()
            case 2:
                self.timeConvertToString()
            case 3:
                pass
            case 4:
                
                self.clicked = self.checkButtonClick()
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
                self.draw_triangle(screen)
            case 4:
                self.draw_rectangle(screen)
        

    
    
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



    def checkButtonClick(self):
        mouse_position = pygame.mouse.get_pos()
        if self.hudElement.collidepoint(mouse_position):
            mouse_states = pygame.mouse.get_pressed()
            if mouse_states.index(0):
                return True

    def draw_text(self, screen):
        img = self.hudElement.render(self.text, True, self.color)
        screen.blit(img, (self.position.x, self.position.y))
    
    def draw_triangle(self, screen):
        for TRIANGLE in self.hudElement:
            pygame.draw.polygon(screen, WHITE, TRIANGLE, LINE_WIDTH)
        #pygame.draw.polygon(screen, "white", self.hudElement, LINE_WIDTH)

    def draw_rectangle(self,screen):
        pygame.draw.rect(screen, WHITE, self.hudElement)

    