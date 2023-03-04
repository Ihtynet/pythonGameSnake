"""Движение змейки
Чтобы передвигать змейку, мы будем использовать ключевые события из класса KEYDOWN библиотеки Pygame. События K_UP, K_DOWN, K_LEFT, и K_RIGHT заставят змейку двигаться вверх, вниз, влево и вправо соответственно. Также, цвет дисплея меняется от черного (по умолчанию) до белого при помощи метода fill().

Для сохранения изменений координат x и y мы создали две новых переменные: x1_change и y1_change.
"""
import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game by Pythonist')

game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -5
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 5
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -5
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 5
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()