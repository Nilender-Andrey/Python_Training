import pygame
import sys

STEP = 10

screen_width, screen_height = 800, 600

rect_width, rect_height = 100, 200
rect_x = screen_width/2 - rect_width/2
rect_y = screen_height/2 - rect_height/2
rect_color = pygame.Color("lightYellow")
screen_fill_color = (32, 52, 71)


# clock = pygame.time.Clock()

# Инициализируем
pygame.init()

# Задаем размеры экрана
screen = pygame.display.set_mode((screen_width, screen_height))


# Задаем название
pygame.display.set_caption("My pygame")


# Обрабатываем события
while True:
    for event in pygame.event.get():
        # print(event)
        # Закрытие экрана
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y -= STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y += STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP:
                rect_x += STEP

            # Цвет заливки экрана
    screen.fill(screen_fill_color)

   # Рисуем прямоугольник
    pygame.draw.rect(screen, rect_color,
                     (rect_x, rect_y, rect_width, rect_height))
    # Обновляем данные на экране
    pygame.display.update()

    # Количество изменений экрана в секунду
    # clock.tick(5)
