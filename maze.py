import random
import sys
sys.setrecursionlimit(10000)

# Maze dimensions (should be odd for proper walls and paths)
WIDTH = 16
HEIGHT = 16

# Maze initialization
maze = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Directions (N, S, E, W)
directions = [(-2, 0), (2, 0), (0, 2), (0, -2)]

# Recursive DFS Maze Generator
def generate_maze(x, y):
    maze[y][x] = ' '
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 < nx < WIDTH-1 and 0 < ny < HEIGHT-1 and maze[ny][nx] == '#':
            maze[y + dy//2][x + dx//2] = ' '
            generate_maze(nx, ny)

# Maze Solver using DFS
def solve_maze(x, y, path):
    if maze[y][x] == 'E':
        return True
    if maze[y][x] != ' ' and maze[y][x] != 'S':
        return False

    maze[y][x] = '.'
    path.append((x, y))

    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if solve_maze(x + dx, y + dy, path):
            return True

    path.pop()
    maze[y][x] = ' '
    return False

# Set start and end
def set_start_end():
    maze[1][1] = 'S'
    maze[HEIGHT-2][WIDTH-2] = 'E'

# Print maze
def print_maze():
    for row in maze:
        print(''.join(row))

# Run everything
generate_maze(1, 1)
set_start_end()
path = []
solve_maze(1, 1, path)
print_maze()
