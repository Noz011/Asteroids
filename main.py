import pygame
from game_states.menu_state import MenuState
from game_states.game_state import GameState
from game_states.death_state import DeathState
from bin.constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    states = {
        "menu" : MenuState(),
        "game" : GameState(),
        "death": DeathState()
    }

    current = states["menu"]
    running = True
    
    while(running):
        dt = clock.tick(60) / 1000


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                next_state = current.handle_event(event)
                if next_state:
                    current = states[next_state]
        
        next_state = current.update(dt)
        if next_state:
            current = states[next_state]

        current.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()