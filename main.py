import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    reloj = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    jugador = Player(x, y)
    campoasteroides = AsteroidField()
    dt = 0

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
        updatable.update(dt)

        for asteroid in asteroids:
              for shot in shots:
                    if asteroid.collision(shot):
                          asteroid.split()
                          shot.kill()
              if asteroid.collision(jugador):
                    print("Game over!")
                    sys.exit()

        screen.fill("black")
        #jugador.draw(screen)
        #jugador.update(dt)
        for obj in drawable:
              obj.draw(screen)
              
        pygame.display.flip()
        dt = reloj.tick(60) / 1000
        

if __name__  == "__main__":
        main()  