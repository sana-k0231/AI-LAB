import heapq
print("SANA KISHOR 1BF24CS270")
# Calculate h(n): Manhattan Distance
def h(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            # Current position
            row1 = i // 3
            col1 = i % 3

            # Goal position
            j = goal.index(state[i])
            row2 = j // 3
            col2 = j % 3

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


# Print puzzle state
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def a_star(start, goal):

    # g(n) = 0
    g = 0

    # f(n) = g(n) + h(n)
    f = g + h(start, goal)

    # Priority queue
    pq = [(f, g, start, [start])]

    visited = set()

    while pq:

        # Remove state with smallest f(n)
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        # Check goal
        if state == goal:
            print("Solution Path:")
            for s in path:
                print_state(s)

            print("Total moves =", g)
            return

        # Find blank tile
        blank = state.index(0)

        row = blank // 3
        col = blank % 3

        # Possible moves: Up, Down, Left, Right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:

            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:

                new_blank = new_row * 3 + new_col

                # Create new state
                new_state = list(state)

                # Move blank
                new_state[blank], new_state[new_blank] = \
                    new_state[new_blank], new_state[blank]

                new_state = tuple(new_state)

                if new_state not in visited:

                    # g = g + 1
                    new_g = g + 1

                    # h = Manhattan Distance
                    new_h = h(new_state, goal)

                    # f = g + h
                    new_f = new_g + new_h

                    # Add to priority queue
                    heapq.heappush(
                        pq,
                        (new_f, new_g, new_state, path + [new_state])
                    )


# Initial state
start = (
    2, 8, 3,
    1, 6, 4,
    7, 0, 5
)

# Goal state
goal = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)

# Run A*
a_star(start, goal)