import asteroid
import asteroidfield
import constants
import player
import pygame
import shot
import sys


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    shot.Shot.containers = (shots, updatable, drawable)
    newplayer = player.Player(
        x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2
    )
    astfield = asteroidfield.AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for ast in asteroids:
            if ast.collide(newplayer):
                print("Game Over!")
                sys.exit(0)
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        # Limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds


if __name__ == "__main__":
    main()
