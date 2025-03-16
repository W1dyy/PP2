import pygame
import time
import math


pygame.init()


WIDTH, HEIGHT = 1400, 1050 
CLOCK_CENTER = (WIDTH // 2, HEIGHT // 2)


clock_face = pygame.image.load("clock.png")
right_hand = pygame.image.load("rightarm.png")  
left_hand = pygame.image.load("leftarm.png")  



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amir maded Clock")

def rotate_hand(image, angle, pivot):

    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rect


running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(clock_face, (0, 0))  

    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

   
    minute_angle = -(minutes * 6)  
    second_angle = -(seconds * 6)  

   
    right_rotated, right_pos = rotate_hand(right_hand, minute_angle, CLOCK_CENTER)
    left_rotated, left_pos = rotate_hand(left_hand, second_angle, CLOCK_CENTER)

    screen.blit(right_rotated, right_pos)
    screen.blit(left_rotated, left_pos)

   
    pygame.display.flip()

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000) 

pygame.quit()
