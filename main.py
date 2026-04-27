import pygame
from constants import *
from logger import log_state ,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\n"
          f" Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    

    while True:
        log_state()

        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black")

        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds



if __name__ == "__main__":
    main()
