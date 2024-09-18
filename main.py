import pygame
import sys
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    afield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update objects
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if(player.collides(asteroid))
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if(bullet.collides(asteroid)) # concurrent list mod: pygame or python must handle somehow
                    asteroid.split()
                    bullet.kill()

        # draw
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        #limit to 60 fps
        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
