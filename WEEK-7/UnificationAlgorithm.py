
# Unification Algorithm in Artificial Intelligence

# Check whether a term is a variable
def is_variable(x):
    return isinstance(x, str) and x[0].islower()


# Apply substitution to a term
def apply_substitution(term, subst):

    if isinstance(term, str):
        while term in subst:
            term = subst[term]
        return term

    return tuple(apply_substitution(x, subst) for x in term)


# Check whether variable occurs in a term
def occurs(var, term, subst):

    term = apply_substitution(term, subst)

    if var == term:
        return True

    if isinstance(term, tuple):
        return any(occurs(var, x, subst) for x in term)

    return False


# Unification function
def unify(x, y, subst):

    x = apply_substitution(x, subst)
    y = apply_substitution(y, subst)

    # If both are identical
    if x == y:
        return subst

    # If x is a variable
    if is_variable(x):

        if occurs(x, y, subst):
            return None

        subst[x] = y
        return subst

    # If y is a variable
    if is_variable(y):

        if occurs(y, x, subst):
            return None

        subst[y] = x
        return subst

    # If both are compound expressions
    if isinstance(x, tuple) and isinstance(y, tuple):

        if len(x) != len(y):
            return None

        for a, b in zip(x, y):
            subst = unify(a, b, subst)

            if subst is None:
                return None

        return subst

    # Otherwise unification fails
    return None


# Main Program
print("UNIFICATION ALGORITHM")

# Two predicates
P1 = ("Knows", "x", "John")
P2 = ("Knows", "Mary", "y")

print("\nFirst Predicate:", P1)
print("Second Predicate:", P2)

# Initialize substitution set
SUBST = {}

# Call unification function
result = unify(P1, P2, SUBST)

# Display result
if result is not None:
    print("\nUnification Successful!")
    print("Substitution Set (SUBST):")

    for key, value in result.items():
        print(key, "=", value)

else:
    print("\nUnification Failed!")
