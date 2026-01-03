import pygame
import constants
from logger import log_state
import player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    
    pygame.init()
    clocktime = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    player_ship = player.Player((constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_ship.update(dt)
        player_ship.draw(screen)
        pygame.display.flip()
        dt = clocktime.tick(60) / 1000



if __name__ == "__main__":
    main()
