import pygame

# pygame 초기화 필요
pygame.init()
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

# 기본 설정
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT_SIZE = 50

TILE_SIZE = min(screen_width, screen_height) // 12
WIDTH, HEIGHT = lambda x : TILE_SIZE * x, lambda x: TILE_SIZE * x