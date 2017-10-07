import pygame
import random
import sys
import math

radius = 0
x, y = 0, 0
red = int(random.random()*255)
green = int(random.random()*255)
blue = int(random.random()*255)
background = 0
color = 0
fig = 0
newFig = 0

pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window.fill(pygame.Color(255, 255, 255))

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

fps = pygame.time.Clock()

x = width/2
y = height/2
xFlag = 0
yFlag = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    movX = random.choice([10,20,30,40,50])
    if xFlag == 0 and x<width:
        x += movX
    elif x >= width:
        xFlag = 1
        x -= movX
    elif xFlag == 1 and x>0:
        x -= movX
    else:
        xFlag = 0
        x += movX

    movY = random.choice([10,20,30,40,50])
    if yFlag == 0 and y<height:
        y += movY
    elif y >= height:
        yFlag = 1
        y -= movY
    elif yFlag == 1 and y>0:
        y -= movY
    else:
        yFlag = 0
        y += movY

    color = int(random.random()*20)
    if color == 0:
        red = 255
        green = 0
        blue = 0
    elif color == 1:
        red = 0
        green = 255
        blue = 0
    elif color == 2:
        red = 0
        green = 0
        blue == 255
    elif color == 3:
        red = int(random.random()*255)
        green = int(random.random()*255)
        blue = int(random.random()*255)


    background = int(random.random()*100)
    if background == 0:
        window.fill(pygame.Color(255, 255, 255))
        if red > 180 and green > 180 and blue > 180:
            red = int(random.random()*255)
            green = int(random.random()*255)
            blue = int(random.random()*255)
    elif background == 1:
        window.fill(pygame.Color(0, 0, 0))
        if red < 80 and green < 80 and blue < 80:
            red = int(random.random()*255)
            green = int(random.random()*255)
            blue = int(random.random()*255)

    fig = int(random.random()*50)
    if fig < 3:
        newFig = fig    
    
    radius = (abs(width/2-x)+abs(height/2-y))/2 + 1
    S = math.sqrt(2*(radius*radius))
    T = S - radius
    offset = math.sqrt((T*T)/2)

    if newFig == 0:
        pygame.draw.circle(window, pygame.Color(red, green , blue), (x, y), radius, 1)
    elif newFig == 1:
        pygame.draw.rect(window, pygame.Color(red, green , blue), (x - radius + offset, y - radius + offset, 2*radius-2*offset, 2*radius-2*offset), 1)
    elif newFig == 2:
        pygame.draw.circle(window, pygame.Color(red, green , blue), (x, y), radius, 1)
        pygame.draw.rect(window, pygame.Color(red, green , blue), (x - radius + offset, y - radius + offset, 2*radius-2*offset, 2*radius-2*offset), 1)
        
    pygame.display.update()
    fps.tick(20)




