from unicodedata import decimal

import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()



    Player.containers = (updatable, drawable)
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable)


    AsteroidField.containers = (updatable)

    field = AsteroidField()

    while True:
        log_state()
        screen.fill("black")
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
