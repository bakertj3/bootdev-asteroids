from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_vector_1 = self.velocity.rotate(angle)
            new_vector_2 = self.velocity.rotate((-1) * angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_1.velocity = new_vector_1 * 1.2
            child_2 = Asteroid(self.position.x, self.position.y, new_radius)
            child_2.velocity = new_vector_2 * 1.2
            
