
from itertools import combinations

# Calculate the number of attacking pairs
def cost(state):
    n = len(state)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Same row or same diagonal
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


# Generate neighbours by swapping two queen positions
def get_neighbours(state):
    neighbours = []

    for i, j in combinations(range(len(state)), 2):
        new_state = state.copy()

        # Swap positions of two queens
        new_state[i], new_state[j] = new_state[j], new_state[i]

        neighbours.append((new_state, (i, j), cost(new_state)))

    return neighbours


# Hill Climbing Algorithm
def hill_climbing(initial_state):
    current = initial_state.copy()
    step = 1

    print("Initial State:", current)
    print("Initial Cost:", cost(current))

    while True:
        print("\n" + "=" * 50)
        print("STEP", step)
        print("Current State:", current)
        print("Current Cost:", cost(current))

        neighbours = get_neighbours(current)

        print("\nNeighbour States:")

        for state, pair, value in neighbours:
            print(f"Swap {pair}: {state} -> Cost = {value}")

        # Select the neighbour with minimum cost.
        # combinations() ensures lexicographical tie-breaking.
        best = min(neighbours, key=lambda x: x[2])

        next_state, swapped_pair, next_cost = best

        # Stop if no improvement is possible
        if next_cost >= cost(current):
            print("\nNo better neighbour found.")
            print("Algorithm terminated.")
            break

        current = next_state

        print("\nSelected Swap:", swapped_pair)
        print("New State:", current)
        print("New Cost:", next_cost)

        step += 1

        if next_cost == 0:
            print("\nGoal State Reached!")
            break

    print("\nFinal Configuration:", current)
    print("Final Cost:", cost(current))


# Main program
initial_state = [3, 1, 2, 0]

hill_climbing(initial_state)
