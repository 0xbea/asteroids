import circleshape
import constants
import pygame


class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = constants.SHOT_RADIUS

    def draw(self, screen):
        # Draw the shot as a circle
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        # Move the shot in the direction of its velocity
        self.position += self.velocity * dt
