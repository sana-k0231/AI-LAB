
from itertools import product

# Function to check implication
def implies(a, b):
    return (not a) or b


# Function to evaluate Knowledge Base
def evaluate_kb(P, Q, R):

    sentence1 = implies(Q, P)       # Q -> P
    sentence2 = implies(P, not Q)   # P -> not Q
    sentence3 = Q or R              # Q OR R

    kb = sentence1 and sentence2 and sentence3

    return sentence1, sentence2, sentence3, kb


# Function to check entailment
def check_entailment(query, models):

    for P, Q, R in models:

        if not query(P, Q, R):
            return False

    return True


# Main Program
print("PROPOSITIONAL LOGIC - TRUTH TABLE ENUMERATION")

print("\nKnowledge Base:")
print("1. Q -> P")
print("2. P -> NOT Q")
print("3. Q OR R")

# Generate all possible truth values
symbols = [True, False]

models = []

print("\nTRUTH TABLE")
print("P\tQ\tR\tQ->P\tP->!Q\tQ|R\tKB")

# Truth table enumeration
for P, Q, R in product(symbols, repeat=3):

    s1, s2, s3, kb = evaluate_kb(P, Q, R)

    print(P, Q, R, s1, s2, s3, kb, sep="\t")

    # Store models where KB is true
    if kb:
        models.append((P, Q, R))


# Display KB models
print("\nMODELS WHERE KB IS TRUE:")

for model in models:
    print(model)


# Query 1: Does KB entail R?
q1 = lambda P, Q, R: R

# Query 2: Does KB entail R -> P?
q2 = lambda P, Q, R: implies(R, P)

# Query 3: Does KB entail Q -> R?
q3 = lambda P, Q, R: implies(Q, R)


print("\nENTAILMENT RESULTS")

if check_entailment(q1, models):
    print("1. KB entails R: YES")
else:
    print("1. KB entails R: NO")

if check_entailment(q2, models):
    print("2. KB entails R -> P: YES")
else:
    print("2. KB entails R -> P: NO")

if check_entailment(q3, models):
    print("3. KB entails Q -> R: YES")
else:
    print("3. KB entails Q -> R: NO")
