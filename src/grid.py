import random

def create_puzzle(grid_size):
    numbers = list(range(1, grid_size * grid_size)) + [0]  # 0은 빈 칸
    random.shuffle(numbers)
    if not is_solvable(numbers, grid_size):
        if numbers[-1] == 0:
            numbers[-2], numbers[-3] = numbers[-3], numbers[-2]
        elif numbers[-2] == 0:
            numbers[-3], numbers[-1] = numbers[-1], numbers[-3]
        else:
            numbers[-2], numbers[-1] = numbers[-1], numbers[-2]
    return [numbers[i:i + grid_size] for i in range(0, len(numbers), grid_size)]

def is_solvable(numbers, grid_size):
    inversions = 0
    for i in range(1, len(numbers)):
        if numbers[i] == 0:
            continue
        for j in range(i):
            if numbers[j] > numbers[i]:
                inversions += 1

    if (grid_size % 2 == 1) and (inversions % 2 == 0): return True
    elif (grid_size % 2 == 0):
        if ((grid_size - numbers.index(0) // grid_size) % 2 == 0) and (inversions % 2 == 1): return True
        elif ((grid_size - numbers.index(0) // grid_size) % 2 == 1) and (inversions % 2 == 0): return True
    else: return False

def find_empty_tile(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                return row, col

def move_tile(grid, row, col, empty_row, empty_col):
    grid[empty_row][empty_col], grid[row][col] = grid[row][col], grid[empty_row][empty_col]
