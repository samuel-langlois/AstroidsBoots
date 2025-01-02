# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main ():
    # initialize pygame
    pygame.init()
    # remove below later?
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # remove above later?
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill((0,0,0), rect=None, special_flags=0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
if __name__ == "__main__":
    main()
