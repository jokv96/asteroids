from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        direction = random.uniform(20,50)
        ast1 = self.velocity.rotate(direction)
        ast2 = self.velocity.rotate(-direction)
        new_size = self.radius - ASTEROID_MIN_RADIUS
        ast1_init = Asteroid(self.position[0], self.position[1], new_size)
        ast2_init = Asteroid(self.position[0], self.position[1], new_size)
        ast1_init.velocity = ast1 * 1.2
        ast2_init.velocity = ast2 * 1.2
