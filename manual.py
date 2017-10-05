import pygame
import random
import sys

radius = 0
mouseX, mouseY = 0, 0
red = int(random.random()*255)
green = int(random.random()*255)
blue = int(random.random()*255)
LEFT = 1
RIGHT = 3
fig = 0 #0 circulo 1 rectangulo

pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window.fill(pygame.Color(255, 255, 255))

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

fps = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            window.fill(pygame.Color(255, 255, 255))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            window.fill(pygame.Color(0, 0, 0))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            red = 255
            green = 0
            blue = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            red = 0
            green = 255
            blue = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            red = 0
            green = 0
            blue = 255
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            red = int(random.random()*255)
            green = int(random.random()*255)
            blue = int(random.random()*255)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            fig = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            fig = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            fig = 2

    radius = (abs(width/2-mouseX)+abs(height/2-mouseY))/2 + 1
    if fig == 0:
        pygame.draw.circle(window, pygame.Color(red, green , blue), (mouseX, mouseY), radius, 1)
    elif fig == 1:
        pygame.draw.rect(window, pygame.Color(red, green , blue), (mouseX-radius/2, mouseY-radius/2, radius, radius), 1)
    else:
        pygame.draw.circle(window, pygame.Color(red, green , blue), (mouseX, mouseY), radius, 1)
        pygame.draw.rect(window, pygame.Color(red, green , blue), (mouseX-radius/2, mouseY-radius/2, radius, radius), 1)
        
    pygame.display.update()
    fps.tick(30)