# Hill Climbing Algorithm for 4-Queens Problem

N = 4

# Function to calculate the cost
def calculate_cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            # Check same row or diagonal
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):

                conflicts += 1

    return conflicts


# Function to generate neighbouring states
def generate_neighbors(state):
    neighbors = []

    for col in range(N):
        for row in range(N):

            if row != state[col]:
                new_state = state.copy()
                new_state[col] = row

                neighbors.append(new_state)

    return neighbors


# Function to display the chessboard
def display_board(state):
    for row in range(N):
        for col in range(N):

            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")

        print()


# Hill Climbing Algorithm
def hill_climbing():

    # Initial state
    current_state = [0, 0, 0, 0]

    print("Initial State:", [x + 1 for x in current_state])

    while True:

        current_cost = calculate_cost(current_state)

        print("\nCurrent State:",
              [x + 1 for x in current_state])
        print("Current Cost:", current_cost)

        # Check goal state
        if current_cost == 0:
            print("\nGoal State Reached!")
            break

        # Generate neighbours
        neighbors = generate_neighbors(current_state)

        best_state = None
        best_cost = float('inf')

        print("\nNeighbor States and Costs:")

        for neighbor in neighbors:

            cost = calculate_cost(neighbor)

            print([x + 1 for x in neighbor],
                  "-> Cost:", cost)

            if cost < best_cost:
                best_cost = cost
                best_state = neighbor

        # Check for local minimum
        if best_cost >= current_cost:
            print("\nLocal Minimum Reached!")
            print("Solution Not Found.")
            return

        # Move to the best neighbour
        current_state = best_state

        print("\nBest Neighbor:",
              [x + 1 for x in current_state])
        print("Best Cost:", best_cost)

    # Display final solution
    print("\nFinal Solution:",
          [x + 1 for x in current_state])

    print("\nFinal Chessboard:")
    display_board(current_state)


# Main function
hill_climbing()
