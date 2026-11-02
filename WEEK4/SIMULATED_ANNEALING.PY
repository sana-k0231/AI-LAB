import random
import math

N = 8

# Calculate number of attacking queen pairs
def calculate_cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):

                conflicts += 1

    return conflicts


# Display chessboard
def display_board(state):
    for row in range(N):
        for col in range(N):

            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")

        print()


# Simulated Annealing Algorithm
def simulated_annealing():

    random.seed(42)

    # Generate initial random state
    current_state = [random.randint(0, N - 1)
                     for _ in range(N)]

    current_cost = calculate_cost(current_state)

    temperature = 10.0
    cooling_rate = 0.995
    steps = 0

    print("Initial State:",
          [x + 1 for x in current_state])
    print("Initial Cost:", current_cost)

    # Simulated Annealing
    while temperature > 0.01 and steps < 10000:

        if current_cost == 0:
            break

        # Generate random neighbour
        new_state = current_state.copy()

        col = random.randint(0, N - 1)
        row = random.randint(0, N - 1)

        while row == new_state[col]:
            row = random.randint(0, N - 1)

        new_state[col] = row

        new_cost = calculate_cost(new_state)

        # Calculate cost difference
        delta = new_cost - current_cost

        # Accept or reject the new state
        if delta < 0:
            current_state = new_state
            current_cost = new_cost

        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                current_state = new_state
                current_cost = new_cost

        # Reduce temperature
        temperature *= cooling_rate
        steps += 1

    # Display result
    if current_cost == 0:

        print("\nSolution Found!")
        print("Number of Steps:", steps)

        print("\nFinal State:",
              [x + 1 for x in current_state])

        print("Final Cost:", current_cost)

        print("\nFinal Chessboard:")
        display_board(current_state)

    else:
        print("\nSolution Not Found!")


# Main function
simulated_annealing()
