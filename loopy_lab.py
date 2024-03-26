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
width, height = 1200, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Loopy Lab")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics
    # --(YOUR CODE STARTS HERE)-----------------------------------------------
    screen.fill(WHITE)

    # Draw a 50x50 pixel black square with top-left corner at (x, y) = (5, 10)
    pygame.draw.rect(screen, BLACK, pygame.Rect(5, 10, 50, 50))





    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
