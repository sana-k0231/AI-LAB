
import random
import math

# Cost function
def cost(state):
    return state ** 2


# Generate a random neighbour
def random_neighbour(current):
    return current + random.choice([-1, 1])


# Simulated Annealing Algorithm
def simulated_annealing():

    # Step 1: Initial state
    current = random.randint(-10, 10)

    # Step 2: Initial temperature
    T = 100

    # Cooling rate
    cooling_rate = 0.95

    print("Initial State:", current)

    # Step 3: Repeat while temperature > 0
    while T > 0.1:

        # Step 4: Generate random neighbour
        next_state = random_neighbour(current)

        # Step 5: Calculate change in cost
        delta_E = cost(current) - cost(next_state)

        # Step 6: If improvement, accept next state
        if delta_E > 0:
            current = next_state

        # Step 7: Otherwise accept with probability
        else:
            probability = math.exp(delta_E / T)

            if random.random() < probability:
                current = next_state

        # Step 8: Decrease temperature
        T = T * cooling_rate

    # Step 9: Return final state
    return current


# Main Program
print("SIMULATED ANNEALING ALGORITHM")

result = simulated_annealing()

print("\nFinal State:", result)
print("Final Cost:", cost(result))
