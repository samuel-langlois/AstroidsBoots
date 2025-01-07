# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main ():
    # initialize pygame
    pygame.init()
    score = 0

    # remove below later?
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # remove above later?

    # Initislize the Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    font = pygame.font.Font(None, 36)
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    # Set the sprites to ether {updatable} and/or {drawable}
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable

    # Create the objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None, special_flags=0)
        
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.colliding(player):
                print("Game Over!!")
                return
            for s in shots:
                if s.colliding(a):
                    s.kill()
                    score += a.split()
            
        for d in drawable:
            d.draw(screen)
        text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text_surface, (0, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
