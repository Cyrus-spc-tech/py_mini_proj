import heapq
from collections import defaultdict

def a_star(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan

    def neighbors(pos):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
        return [(pos[0] + d[0], pos[1] + d[1]) for d in dirs
                if 0 <= pos[0] + d[0] < len(grid) and 0 <= pos[1] + d[1] < len(grid[0])
                and grid[pos[0] + d[0]][pos[1] + d[1]] == 0]

    open_set = []
    heapq.heappush(open_set, (0, start))  # (f, node)
    came_from = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse to start->goal

        for neighbor in neighbors(current):
            tentative_g = g_score[current] + 1  # Assume cost=1
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                if neighbor not in [n[1] for n in open_set]:  # Simple check; better with set
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
print(a_star(grid, (0, 0), (4, 4)))  # Possible output: [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3), (2,4), (3,4), (4,4)]