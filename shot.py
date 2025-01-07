import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        print("Shot created!")  # Debug print
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        print("Shot draw called!")  # Debug print
        pygame.draw.circle(screen, (255,0,0), self.position, SHOT_RADIUS/2, 2)
    
    def update(self, dt):
        print("Shot update called!")  # Debug print
        self.position += (self.velocity * dt)