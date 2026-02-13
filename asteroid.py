from constants import *
from circleshape import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            asteroid_one_vector = self.velocity.rotate(new_angle)
            asteroid_two_vector = -(self.velocity.rotate(new_angle))
            new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position[0], self.position[1], new_asteroids_radius)
            asteroid_two = Asteroid(self.position[0], self.position[1], new_asteroids_radius)
            asteroid_one.velocity = asteroid_one_vector * 1.2
            asteroid_two.velocity = asteroid_two_vector * 1.2
