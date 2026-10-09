def dls(state, goal, depth, path):
    if state == goal:
        return path + [state]
    if depth == 0:
        return None

    zero = state.index(0)
    r, c = divmod(zero, 3)

    moves = []
    if r > 0: moves.append(zero - 3)
    if r < 2: moves.append(zero + 3)
    if c > 0: moves.append(zero - 1)
    if c < 2: moves.append(zero + 1)

    for m in moves:
        new = state.copy()
        new[zero], new[m] = new[m], new[zero]

        if new not in path:
            result = dls(new, goal, depth - 1, path + [state])
            if result:
                return result
    return None


def idfs(start, goal):
    for depth in range(20):
        result = dls(start, goal, depth, [])
        if result:
            return result
    return None


start = [1 ,2, 3,
4 ,0, 6,
7,5 ,8]


goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

result = idfs(start, goal)

for state in result:
    print(state[:3])
    print(state[3:6])
    print(state[6:])
    print()