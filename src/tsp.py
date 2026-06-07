import math


def route_distance(points, route):
    total = 0.0
    for a, b in zip(route, route[1:]):
        total += _distance(points[a], points[b])
    return total


def solve_tsp(points, return_to_start=True):
    """
    Resolve o TSP para uma lista de pontos (x, y).
    Para ate 15 pontos usa Held-Karp exato; acima disso usa vizinho mais
    proximo com refinamento 2-opt.
    Retorna (rota_de_indices, distancia).
    """
    if not points:
        return [], 0.0
    if len(points) == 1:
        return [0, 0] if return_to_start else [0], 0.0

    if len(points) <= 15:
        route = _held_karp(points, return_to_start)
    else:
        route = _nearest_neighbor(points, return_to_start)
        route = _two_opt(points, route)

    return route, route_distance(points, route)


def _distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _held_karp(points, return_to_start):
    n = len(points)
    distances = [[_distance(points[i], points[j]) for j in range(n)] for i in range(n)]
    costs = {}

    for node in range(1, n):
        costs[(1 << node, node)] = (distances[0][node], 0)

    for subset_size in range(2, n):
        for subset in _subsets(range(1, n), subset_size):
            mask = 0
            for node in subset:
                mask |= 1 << node

            for last in subset:
                previous_mask = mask ^ (1 << last)
                candidates = [
                    (costs[(previous_mask, prev)][0] + distances[prev][last], prev)
                    for prev in subset
                    if prev != last
                ]
                costs[(mask, last)] = min(candidates)

    full_mask = (1 << n) - 2
    if return_to_start:
        final_cost, last = min(
            (costs[(full_mask, node)][0] + distances[node][0], node)
            for node in range(1, n)
        )
    else:
        final_cost, last = min((costs[(full_mask, node)][0], node) for node in range(1, n))

    route = [last]
    mask = full_mask
    while mask:
        _, previous = costs[(mask, last)]
        mask ^= 1 << last
        if previous == 0:
            break
        route.append(previous)
        last = previous

    route = [0] + list(reversed(route))
    if return_to_start:
        route.append(0)

    # final_cost is computed above to choose the best ending node.
    _ = final_cost
    return route


def _subsets(items, size):
    items = list(items)
    if size == 0:
        yield ()
    elif len(items) >= size:
        first, rest = items[0], items[1:]
        for subset in _subsets(rest, size - 1):
            yield (first,) + subset
        yield from _subsets(rest, size)


def _nearest_neighbor(points, return_to_start):
    unvisited = set(range(1, len(points)))
    route = [0]

    while unvisited:
        current = route[-1]
        next_node = min(unvisited, key=lambda node: _distance(points[current], points[node]))
        route.append(next_node)
        unvisited.remove(next_node)

    if return_to_start:
        route.append(0)
    return route


def _two_opt(points, route):
    if len(route) < 5:
        return route

    improved = True
    best = route[:]
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best) - 1):
                if j - i == 1:
                    continue
                candidate = best[:i] + best[i:j][::-1] + best[j:]
                if route_distance(points, candidate) < route_distance(points, best):
                    best = candidate
                    improved = True
        route = best
    return best
