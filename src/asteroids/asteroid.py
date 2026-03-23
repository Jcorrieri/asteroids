import pygame
import random

from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid split")

        theta = random.uniform(20, 50)
        first_child_vel = self.velocity.rotate(theta)
        second_child_vel = self.velocity.rotate(-theta)

        child_radii = self.radius - ASTEROID_MIN_RADIUS

        first_child = Asteroid(self.position.x, self.position.y, child_radii)
        first_child.velocity  = first_child_vel * 1.2

        second_child = Asteroid(self.position.x, self.position.y, child_radii)
        second_child.velocity  = second_child_vel * 1.2

