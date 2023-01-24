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
    white = (255, 255, 255)

    #initial state of the traffic light
    current_state = "red"

    clock = pygame.time.Clock()

    

    #Program exit garnako lagi
    run = True
    while run:
        clock.tick(60)
        screen.fill(white)
        pygame.draw.line(screen, black, (350,100), (450,100))
        pygame.draw.line(screen, black, (350,400), (450,400))
        pygame.draw.line(screen, black, (350,100), (350,400))
        pygame.draw.line(screen, black, (450,100), (450,400))
        pygame.draw.line(screen, black, (350,200), (450,200))
        pygame.draw.line(screen, black, (350,300), (450,300))
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