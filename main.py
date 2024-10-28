# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = []
    drawable = []
    updatable.append(player)
    drawable.append(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        for object in drawable:
            object.draw(screen)
        
        for object in updatable:
            object.update(dt)

        pygame.display.flip()

if __name__ == "__main__":
    main()