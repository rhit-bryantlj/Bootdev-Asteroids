from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x,y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        temp_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(-temp_angle)
        v2 = self.velocity.rotate(temp_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid1.velocity = v1 * 1.2
        asteroid2.velocity = v2 * 1.2
