import random
import matplotlib.pyplot as plt

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

N = 8
cx = [1, 1, 2, 2, -1, -1, -2, -2]
cy = [2, -2, 1, -1, 2, -2, 1, -1]

knight_moves = []

def limits(x, y):
    return ((x >= 0 and y >= 0) and (x < N and y < N))

def isempty(a, x, y):
    return (limits(x, y)) and (a[y * N + x] < 0)

def getDegree(a, x, y):
    count = 0
    for i in range(N):
        if isempty(a, (x + cx[i]), (y + cy[i])):
            count += 1
    return count

def nextMove(a, cell):
    min_deg_idx = -1
    c = 0
    min_deg = (N + 1)
    nx = 0
    ny = 0
    start = random.randint(0, N-1)
    for count in range(0, N):
        i = (start + count) % N
        nx = cell.x + cx[i]
        ny = cell.y + cy[i]
        c = getDegree(a, nx, ny)
        if ((isempty(a, nx, ny)) and c < min_deg):
            min_deg_idx = i
            min_deg = c
    if (min_deg_idx == -1):
        return None
    nx = cell.x + cx[min_deg_idx]
    ny = cell.y + cy[min_deg_idx]
    a[ny * N + nx] = a[(cell.y) * N + (cell.x)] + 1

    cell.x = nx
    cell.y = ny

    knight_moves.append((nx, ny))

    return cell

def neighbour(x, y, xx, yy):
    for i in range(N):
        if ((x + cx[i]) == xx) and ((y + cy[i]) == yy):
            return True
    return False

def findClosedTour():
    a = [-1] * N * N
    sx = 0
    sy = 0
    knight_moves.append((sx, sy))
    cell = Cell(sx, sy)

    a[cell.y * N + cell.x] = 1
    ret = None
    for i in range(N * N - 1):
        ret = nextMove(a, cell)
        if ret == None:
            return False

    if not neighbour(ret.x, ret.y, sx, sy):
        return False

    board = [[0 for _ in range(N)] for _ in range(N)]
    for move_num, move in enumerate(knight_moves):
        x, y = move
        board[y][x] = move_num + 1

    plt.figure(figsize=(8, 8))
    plt.imshow(board, cmap='viridis', interpolation='nearest')
    plt.title("Knight's Tour")

    for i, move in enumerate(knight_moves):
        x, y = move
        plt.text(x, y, str(i + 1), ha='center', va='center', color='white', fontsize=14, fontweight='bold')

    for i in range(len(knight_moves) - 1):
        x1, y1 = knight_moves[i]
        x2, y2 = knight_moves[i + 1]
        plt.plot([x1, x2], [y1, y2], color='white', linewidth=2)
    plt.show()
    plt.savefig('answer.png')
    plt.close()
    return True

if __name__ == '__main__':
    while not findClosedTour():
        knight_moves = []
