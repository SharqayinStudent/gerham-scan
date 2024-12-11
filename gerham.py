import math

def cross(o, a, b):
    """Вычисляет векторное произведение векторов OA и OB.
    Положительное значение — поворот против часовой стрелки,
    отрицательное — по часовой стрелке, 0 — если точки коллинеарны."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points):
    # Находим точку с минимальной координатой Y (и минимальной координатой X, если Y одинаковые)
    points = sorted(points)
    start = points[0]
    
    # Сортируем все остальные точки по углу относительно точки start
    def angle_from_start(p):
        return math.atan2(p[1] - start[1], p[0] - start[0])

    sorted_points = sorted(points[1:], key=angle_from_start)

    # Стек для построения конвексной оболочки
    stack = [start, sorted_points[0]]

    for point in sorted_points[1:]:
        while len(stack) > 1 and cross(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)

    return stack


