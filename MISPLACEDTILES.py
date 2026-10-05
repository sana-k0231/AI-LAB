import heapq
print("SANA KISHOR 1BF24CS270")
# Heuristic: number of misplaced tiles
def h(state, goal):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def a_star(start, goal):

    # Priority queue: (f, g, state, path)
    pq = []
    heapq.heappush(pq, (h(start, goal), 0, start, [start]))

    visited = set()

    while pq:

        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        # Goal test
        if state == goal:
            print("Solution Path:")
            for s in path:
                print_state(s)
            print("Total moves =", g)
            return

        # Position of blank tile
        blank = state.index(0)
        row = blank // 3
        col = blank % 3

        # Up, Down, Left, Right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:

            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:

                new_blank = new_row * 3 + new_col

                new_state = list(state)

                # Move blank
                new_state[blank], new_state[new_blank] = \
                    new_state[new_blank], new_state[blank]

                new_state = tuple(new_state)

                if new_state not in visited:

                    new_g = g + 1
                    new_h = h(new_state, goal)
                    new_f = new_g + new_h

                    heapq.heappush(
                        pq,
                        (new_f, new_g, new_state, path + [new_state])
                    )


# Initial state from the question
start = (
    2, 8, 3,
    1, 6, 4,
    7, 0, 5
)

# Goal state from the question
goal = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)

# Run A*
a_star(start, goal)