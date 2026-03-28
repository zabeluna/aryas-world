# src/pathfinding.py
import heapq

def astar(grid, start, goal):
    """
    A* pathfinding em grid 2D.
    grid: lista de listas onde 0 = livre, 1 = obstáculo
    start/goal: tuplas (col, row)
    Retorna lista de (col, row) do caminho, ou [] se impossível.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def h(a, b):  # Heurística Manhattan
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(node):
        x, y = node
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]  # 4 direções
        result = []
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == 0:
                result.append((nx, ny))
        return result

    open_set = []
    heapq.heappush(open_set, (0 + h(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstrói caminho
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor in neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + h(neighbor, goal)
                heapq.heappush(open_set, (f, tentative_g, neighbor))

    return []  # Sem caminho