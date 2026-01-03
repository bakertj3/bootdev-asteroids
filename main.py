import pygame
import constants
from logger import log_state, log_event
import player
import asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    
    pygame.init()
    clocktime = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (drawable, updatable)

    AsteroidField.containers = (updatable)

    new_asteroid_field = AsteroidField()

    player_ship = player.Player((constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for body in asteroids:
            if body.collides_with(player_ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clocktime.tick(60) / 1000



if __name__ == "__main__":
    main()
