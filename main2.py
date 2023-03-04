
"""
Теперь, запустив этот код, вы увидите, что экран не пропадает, как раньше. На нем будут отображаться все действия игры.
Мы этого добились благодаря функции event.get(). Также, при помощи функции display.set_caption(), мы вывели заголовок нашего экрана — ‘Snake game by Pythonist’.

Теперь у нас есть экран для игры, но когда вы кликнете по кнопке close, экран не закроется. Это потому,
что мы не предусмотрели такого поведения. Для решения этой задачи в Pygame предусмотрено событие «QIUT», которое мы используем слеудющим образом:
"""

import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game by Edureka')
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

pygame.quit()
quit()