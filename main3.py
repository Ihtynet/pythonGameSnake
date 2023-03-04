"""Создание змейки
Перед тем как создать змейку, мы инициируем несколько цветовых переменных для раскрашивания самой змейки, еды и экрана.
В Pygame используется цветовая схема RGB (RED, GREEN, BLUE). Установка всех цветов в 0 соответствует черному цвету, а в 255 — соответственно, белому.

Фактически, наша змейка является прямоугольником. Чтобы нарисовать прямоугольник в Pygame, можно воспользоваться функцией draw.rect(),
которая нарисует нам прямоугольник заданного цвета и размера.
"""

import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))

pygame.display.set_caption('Snake game by Pythonist')

blue=(0,0,255)
red=(255,0,0)

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis,blue,[200,150,10,10])
    pygame.display.update()
pygame.quit()
quit()