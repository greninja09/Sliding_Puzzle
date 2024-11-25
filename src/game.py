import pygame
from config import *
from grid import create_puzzle, find_empty_tile, move_tile
from ui import draw_grid, animate_movement
from stages import StageSelection
import tkinter as tk
from timer import Timer


def main():
    pygame.init()

    # 스테이지 선택
    stage_selector = StageSelection()
    grid_size = stage_selector.run()
    if not grid_size:
        return  # 선택이 없으면 종료

    tile_size = TILE_SIZE
    window_width, window_height = WIDTH(grid_size), HEIGHT(grid_size)
    timer_x = screen_width//2 + window_width//2
    timer_y = screen_height//2 - window_height//2

    # pygame 화면 설정
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Sliding Puzzle")
    font = pygame.font.Font(None, tile_size // 3)
    clock = pygame.time.Clock()

    # 퍼즐 생성
    grid = create_puzzle(grid_size)
    running = True

    # 타이머 시작 # TODO: puz_x, y, grid_size넣기
    Timer.start(timer_x, timer_y)

    while running:
        screen.fill(WHITE)
        draw_grid(screen, grid, font)

        # 그리드 업데이트
        pygame.display.flip()

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // tile_size, y // tile_size
                empty_row, empty_col = find_empty_tile(grid)
                if abs(empty_row - row) + abs(empty_col - col) == 1:
                    animate_movement(screen, font, grid, (row, col), (empty_row, empty_col))
                    move_tile(grid, row, col, empty_row, empty_col)

        # 승리 조건 확인
        full = [ [i*grid_size+j+1 for j in range(grid_size)] for i in range(grid_size) ]
        full[-1][-1] = 0
        if grid == full:
            Timer.stop()
            show_solved_message()
            running = False

        clock.tick(FPS)

    pygame.quit()

# 퍼즐 풀이 성공 시 새로운 창을 띄움
def show_solved_message():
    # tkinter 창 생성
    root = tk.Tk()
    root.title("Puzzle Solved!")
    root.geometry("300x150")
    root.eval('tk::PlaceWindow . center')  # 창을 화면 중앙에 배치

    # 메시지 라벨
    label = tk.Label(root, text="Congratulations!\nYou solved the puzzle!", font=("Helvetica", 14))
    label.pack(pady=20)

    # 종료 버튼
    button = tk.Button(root, text="Close", command=root.destroy)
    button.pack(pady=10)

    # tkinter 창 실행
    root.mainloop()

