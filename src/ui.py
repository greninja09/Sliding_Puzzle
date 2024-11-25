import pygame
from config import TILE_SIZE, WHITE, BLACK, GRAY

def draw_grid(screen, grid, font):
    # 기본 그리드와 숫자 출력
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            num = grid[row][col]
            x, y = col * TILE_SIZE, row * TILE_SIZE
            pygame.draw.rect(screen, GRAY if num != 0 else WHITE, (x, y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 2)
            if num != 0:
                text = font.render(str(num), True, BLACK)
                screen.blit(
                    text,
                    (x + TILE_SIZE // 2 - text.get_width() // 2,
                     y + TILE_SIZE // 2 - text.get_height() // 2),
                )

def animate_movement(screen, font, grid, start_pos, end_pos):
    """부드러운 타일 이동 애니메이션"""
    steps = 10
    dx = (end_pos[1] - start_pos[1]) * TILE_SIZE // steps
    dy = (end_pos[0] - start_pos[0]) * TILE_SIZE // steps
    num = grid[start_pos[0]][start_pos[1]]

    for step in range(1, steps + 1):
        screen.fill(WHITE)
        draw_grid(screen, grid, font)  # 기존 타일 그리기

        # 이동 중인 타일
        x = start_pos[1] * TILE_SIZE + dx * step
        y = start_pos[0] * TILE_SIZE + dy * step
        pygame.draw.rect(screen, GRAY, (x, y, TILE_SIZE, TILE_SIZE))
        text = font.render(str(num), True, BLACK)
        screen.blit(
            text,
            (x + TILE_SIZE // 2 - text.get_width() // 2,
             y + TILE_SIZE // 2 - text.get_height() // 2)
        )

        pygame.display.flip()
        pygame.time.delay(30)
