# 8-Puzzle using Iterative Deepening Search (IDS)

# Check if current state is the goal
def is_goal(state, goal):
    return state == goal


# Find the position of blank (0)
def find_blank(state):
    return state.index(0)


# Generate all valid next states
def get_neighbors(state):

    neighbors = []

    blank = find_blank(state)
    row = blank // 3
    col = blank % 3

    # Possible moves: Up, Down, Left, Right
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check whether move is valid
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            # Create new state
            new_state = list(state)

            # Swap blank and tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


# Depth Limited Search
def depth_limited_search(state, goal, depth, path):

    # Check whether goal is reached
    if is_goal(state, goal):
        return path

    # Depth limit reached
    if depth == 0:
        return None

    # Try every valid move
    for new_state in get_neighbors(state):

        # Avoid states already in current path
        if new_state not in path:

            result = depth_limited_search(
                new_state,
                goal,
                depth - 1,
                path + [new_state]
            )

            # If goal found
            if result is not None:
                return result

    # No solution at this depth
    return None


# Iterative Deepening Search
def iterative_deepening_search(initial, goal):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        path = depth_limited_search(
            initial,
            goal,
            depth,
            [initial]
        )

        # Goal found
        if path is not None:
            return path

        # Increase depth
        depth += 1


# Display puzzle
def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])

    print()


# Main program

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

print("Initial State:")
print_puzzle(initial)

print("Goal State:")
print_puzzle(goal)

# Solve using IDS
solution = iterative_deepening_search(initial, goal)

print("Solution Found!")
print("Number of moves:", len(solution) - 1)

print("\nSteps:")

for i, state in enumerate(solution):

    print("Step", i)
    print_puzzle(state)