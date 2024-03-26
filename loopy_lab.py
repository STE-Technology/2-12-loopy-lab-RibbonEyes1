"""
File: loopy_lab.py
Author: Your Name
Date: 2024-XX-XX
Description: Program to generate static graphics patterns using
             Pygame and loops in Python.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Loopy Lab")

# Define colours
WHITE = (255, 255, 255)
MAROON=(117, 15, 39)
ORANGE=(240, 135, 70)
BLACK = (0, 0, 0)
YELLOW=(245, 224, 118)
# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics
    # --(YOUR CODE STARTS HERE)-----------------------------------------------
    screen.fill(MAROON)

    # Draw a 50x50 pixel black square with top-left corner at (x, y) = (5, 10)
    #pygame.draw.rect(screen, BLACK, pygame.Rect(5, 10, 50, 50))

    x_orange=300
    for line in range(2,201,8):
      y_yellow=201
      for x_orange in range (1,y_yellow,8):
        if y_yellow<10:
            y_yellow=y_yellow-8
            pygame.draw.rect(screen,YELLOW,pygame.Rect(line,x_orange,5,5))

   
   
   
   
   
    for line in range(2,201,8):
      for x_orange in range (200,401,8):
    
        pygame.draw.rect(screen,ORANGE,pygame.Rect(line,x_orange,5,5))

    
  
    for line in range(202,402,8):
      
      for x_orange in range (200,401,8):
        if line  :
         WHITE=ORANGE
         pygame.draw.rect(screen,WHITE,pygame.Rect(line,x_orange,5,5))
    
     



    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
