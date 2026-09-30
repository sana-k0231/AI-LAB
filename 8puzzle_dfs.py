# 8-Puzzle using Depth First Search (DFS)

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Generate valid moves
def get_neighbors(state):
    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0), # UP
        (1, 0), # DOWN
        (0, -1), # LEFT
        (0, 1) # RIGHT
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check if move is valid
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


# DFS function
def dfs_8_puzzle(initial, goal):

    stack = [(initial, [initial])]
    visited = set()

    while stack:

        state, path = stack.pop()

        # Check goal
        if state == goal:
            return path

        # Mark state as visited
        if state in visited:
            continue

        visited.add(state)

        # Generate valid moves
        for new_state in get_neighbors(state):

            if new_state not in visited:
                stack.append((new_state, path + [new_state]))

    return None


# Initial and goal states
initial = (
    5, 4, 0,
    6, 1, 8,
    7, 3, 2
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# Display initial state
print("Initial State:")
print_puzzle(initial)

print("Goal State:")
print_puzzle(goal)


# Run DFS
solution = dfs_8_puzzle(initial, goal)


# Display result
if solution:

    print("Solution Found!")
    print("Number of moves:", len(solution) - 1)

    print("\nSteps:")

    for i, state in enumerate(solution):
        print("Step", i)
        print_puzzle(state)

else:
    print("FAILURE: No solution found.")