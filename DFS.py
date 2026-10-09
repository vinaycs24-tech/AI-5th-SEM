def dfs(start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path + [state]

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))
        zero = state.index(0)

        r, c = divmod(zero, 3)
        moves = []

        if r > 0:
            moves.append(zero - 3)  # Up
        if r < 2:
            moves.append(zero + 3)  # Down
        if c > 0:
            moves.append(zero - 1)  # Left
        if c < 2:
            moves.append(zero + 1)  # Right

        for move in moves:
            new_state = state.copy()
            new_state[zero], new_state[move] = (
                new_state[move], new_state[zero]
            )

            if tuple(new_state) not in visited:
                stack.append((new_state, path + [state]))

    return None

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]


goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

result = dfs(start, goal)

if result:
    for state in result:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found")