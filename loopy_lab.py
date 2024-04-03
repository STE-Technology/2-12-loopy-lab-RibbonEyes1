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
GREY=(156, 156, 156)
PURPLE=(163, 103, 149)
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



    """ 
  my attempt at squadrant 1
    what I had tried to do was give the range limit a variable on the y axis
    so that i could try and adjust the height of the loops
    """
# turned out to be an indentation issue
    #QUADRANT 3 FINISHED
    subtract=201
    for line in range(402,602,8):
      subtract=subtract-8
      for y in range (2,subtract,8):
         pygame.draw.rect(screen,YELLOW,pygame.Rect(line,y,5,5))

#QUADRANT 8(FINISHED)
    minus=2
    for line in range (601,801,8):
      minus=minus+8
      for y in range(2,minus,8):
       pygame.draw.rect(screen,PURPLE,pygame.Rect(line,y,5,5))

#QUADRANT 2 (DONE)
       decrease=2
    for line in range(202,401,8):
      decrease=decrease+8
      for x_orange in range(decrease,201,8):
        pygame.draw.rect(screen,YELLOW,pygame.Rect(line,x_orange,5,5))


    
  

#The clashing colours are for identifying the quadrants at a galnce, please excuse the horrible colour theory
#Not to eventually make this more readable

#this is for quadrant on bottom left(FINISHED)
    for line in range(2,201,8):
      for x_orange in range (200,401,8):

        pygame.draw.rect(screen,ORANGE,pygame.Rect(line,x_orange,5,5))


  #for quadrant 6(FINISHED)
    for line in range(202,402,8):
      for opposite in range (200,401,8):
       pygame.draw.rect(screen,PURPLE,pygame.Rect(line,opposite,5,5))
    for line in range(202,402,16):
      for opposite in range (200,401,8):
       pygame.draw.rect(screen,ORANGE,pygame.Rect(line,opposite,5,5))

     
  #for quadrant 7 (FINISHED)
       
    for line in range(402,602,8):
      for opposite in range (200,401,8):
       pygame.draw.rect(screen,YELLOW,pygame.Rect(line,opposite,5,5))
    for line in range(402,602,8):
      for opposite in range (200,401,16):
       pygame.draw.rect(screen,ORANGE,pygame.Rect(line,opposite,5,5))


  #for quadrant 8 (FINISHED)
  #this line if for the yellow horizontal spacing
    for line in range(602,802,8):
     for opposite in range (200,401,16):
       pygame.draw.rect(screen,YELLOW,pygame.Rect(line,opposite,5,5))

  #for the more dispersed while lines
    for line in range(602,802,8):
      for opposite in range (208,401,16):
       pygame.draw.rect(screen,PURPLE,pygame.Rect(line,opposite,5,5))

       #for the verticle (cross stitch )
    for line in range(602,802,16):
      for opposite in range (200,401,8):
       pygame.draw.rect(screen,YELLOW,pygame.Rect(line,opposite,5,5))      
    
  
    
   

  #lines for the quadrants
    pygame.draw.line(screen,GREY,(1,200),(800,200),width=1)
   

    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
