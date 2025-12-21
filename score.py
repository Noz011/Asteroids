import json
import pygame
import string
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Score(pygame.font.Font):
    def __init__(self, x, y, TIMER=False):
        super().__init__(None, 30)
        self.time = 0
        self.text = "0000"
        self.color = "white"
        self.position = pygame.Vector2(x,y)
        self.timer = TIMER
        self.lastJson = {"type": "player_hit"}
        self.__score_list= []

    def update(self):
        if self.timer:
            self.timeConvertToString()
            return
        self.checkShotCollision()

    def draw(self, screen):
        if screen == None:
            print(screen)
            return
        img = self.render(self.text, True, self.color)
        screen.blit(img, (self.position.x, self.position.y))
    

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
