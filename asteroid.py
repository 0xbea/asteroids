import circleshape
import constants
import pygame
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Asteroids move in a straight line at a constant speed
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        child_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        child1 = Asteroid(self.position.x, self.position.y, child_radius)
        child1.velocity = v1 * 1.2
        child2 = Asteroid(self.position.x, self.position.y, child_radius)
        child2.velocity = v2 * 1.2
        return child1, child2
