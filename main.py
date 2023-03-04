"""Создание экрана
Для создания экрана при помощи Pygame нужно воспользоваться функцией display.set_mode(). Также необходимо пользоваться методом init() для инициализации экрана в начале кода и методом quit() для его закрытия в конце. Метод update() используется для применения каких-либо изменений на экране. Еще существует метод flip(), который работает похожим с update() образом. Разница заключается лишь в том, что метод flip() переписывает весь экран целиком, а метод update() применяет именно изменения (хотя если его использовать без параметров, то он тоже переписывает весь экран) .

import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.quit()
quit()
Результат:


Однако, когда вы запустите данный код, экран появится лишь на мгновение, а затем исчезнет. Чтобы исправить эту ошибку,
мы воспользуемся циклом while, который будет работать до окончания игры:
"""
import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game by Pythonist')
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)   # выводит на экран все действия игры

pygame.quit()
quit()