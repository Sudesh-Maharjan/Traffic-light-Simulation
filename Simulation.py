import time
import pygame
# import math

#initialize gareko pygame ko library haru lai
pygame.init()

#Creating a window for the simulation
screen = pygame.display.set_mode((800, 800))

#Display ko caption set gareko
pygame.display.set_caption("Traffic Light System Simulation")

def main():
    #setting the colors of the traffic light
    red = (255, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)

    black = (0, 0, 0)

    #initial state of the traffic light
    current_state = "red"

    clock = pygame.time.Clock()
    #Program exit garnako lagi
    run = True
    while run:
        clock.tick(60)
        screen.fill((0, 0,0))
        #Traffic light screen ma draw garnako lagi
        if current_state == "red":
            pygame.draw.circle(screen, black, (400, 350), 20)
            pygame.draw.circle(screen, black, (400, 250), 20)
            redd = pygame.draw.circle(screen, red, (400, 150), 20)
            pygame.display.update()
            pygame.time.delay(2000)
            current_state = "green"

        elif current_state == "green":
            pygame.draw.circle(screen, black, (400, 150), 20)
            pygame.draw.circle(screen, black, (400, 350), 20)
            greenn = pygame.draw.circle(screen, green, (400, 250), 20)
            pygame.display.update()
            pygame.time.delay(2000)
            current_state = "yellow"

        elif current_state == "yellow":
            pygame.draw.circle(screen, black, (400, 150), 20)
            pygame.draw.circle(screen, black, (400, 250), 20)
            yelloww = pygame.draw.circle(screen, yellow, (400, 350), 20)
            pygame.display.update()
            pygame.time.delay(2000)
            current_state = "red"
    
        #Display lai update garai dine
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            # pygame.quit()
                run = False
        # pygame.display.update()
    pygame.quit()

main()