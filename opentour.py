import matplotlib.pyplot as plt

def get_node(x, y, n):
    return x * n + y

def generate_graph(graph, moves, n):
    for i in range(n):
        for j in range(n):
            curr = get_node(i, j, n)
            
            for move in moves:
                x = i + move[0]
                y = j + move[1]

                if 0 <= x < n and 0 <= y < n:
                    next = get_node(x, y, n)
                    graph[curr].append(next)

    return graph

def print_tour(path, n):
    board = [0 for _ in range(n * n)]

    for i, tiles in enumerate(path):
        board[tiles] = i + 1

    # Visualization part
    fig, ax = plt.subplots()
    ax.set_xticks(range(n+1))
    ax.set_yticks(range(n+1))
    ax.grid(True)

    # Adding color to the chessboard
    light_color = '#f0d9b5'  # Light color
    dark_color = '#b58863'   # Dark color

    def get_color(position):
        row, col = divmod(position, n)
        return light_color if (row + col) % 2 == 0 else dark_color

    for i in range(n):
        for j in range(n):
            ax.fill(
                [j, j + 1, j + 1, j],
                [n - i - 1, n - i - 1, n - i, n - i],
                color=get_color(i * n + j)
            )
            ax.text(j + 0.5, n - i - 0.5, board[i * n + j], ha='center', va='center', fontsize=10)

    for i in range(len(path) - 1):
        current_pos = divmod(path[i], n)
        next_pos = divmod(path[i + 1], n)
        plt.plot([current_pos[1] + 0.5, next_pos[1] + 0.5], [n - current_pos[0] - 0.5, n - next_pos[0] - 0.5], 'ro-')

    plt.show()

def find_path(node, visited, graph, n):
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited, done = find_path(neighbor, visited, graph, n)
            if done:
                return visited, True
            
    if len(visited) == n * n:
        return visited, True
    else:
        visited.pop()
        return visited, False


def open_tour(start_node, graph, n):
    path, done = find_path(start_node, [], graph, n)

    if done:
        print_tour(path, n)
    else:
        print("No solution")


n = 8
graph = {node: [] for node in range(n*n)}
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

graph = generate_graph(graph, moves, n)

x = 0
y = 0

open_tour(get_node(x, y, n), graph, n)