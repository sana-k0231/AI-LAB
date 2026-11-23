
# Forward Chaining in First Order Logic

# Initial facts
facts = {
    ("American", "Robert"),
    ("Missile", "T1"),
    ("Owns", "A", "T1"),
    ("Enemy", "A", "America")
}

# Rules: (premises, conclusion)
rules = [
    (
        [("Missile", "?x")],
        ("Weapon", "?x")
    ),
    (
        [("Missile", "?x"), ("Owns", "A", "?x")],
        ("Sells", "Robert", "?x", "A")
    ),
    (
        [("Enemy", "?x", "America")],
        ("Hostile", "?x")
    ),
    (
        [
            ("American", "?p"),
            ("Weapon", "?q"),
            ("Sells", "?p", "?q", "?r"),
            ("Hostile", "?r")
        ],
        ("Criminal", "?p")
    )
]

# Match a pattern with a fact
def unify(pattern, fact, substitution):
    if len(pattern) != len(fact):
        return None

    sub = substitution.copy()

    for p, f in zip(pattern, fact):
        if p.startswith("?"):
            if p in sub and sub[p] != f:
                return None
            sub[p] = f
        elif p != f:
            return None

    return sub


# Find all possible substitutions
def match_all(premises, facts):
    if not premises:
        return [{}]

    results = []

    first = premises[0]
    remaining = premises[1:]

    for fact in facts:
        sub = unify(first, fact, {})

        if sub is not None:
            new_premises = []

            for premise in remaining:
                new_premises.append(
                    tuple(sub.get(x, x) for x in premise)
                )

            for result in match_all(new_premises, facts):
                combined = sub.copy()
                combined.update(result)
                results.append(combined)

    return results


# Forward Chaining algorithm
def forward_chaining(facts, rules):
    facts = set(facts)

    while True:
        new_facts = set()

        for premises, conclusion in rules:
            substitutions = match_all(premises, facts)

            for sub in substitutions:
                result = tuple(
                    sub.get(x, x) for x in conclusion
                )

                if result not in facts:
                    new_facts.add(result)

        if not new_facts:
            break

        for fact in new_facts:
            print("Derived:", fact)

        facts.update(new_facts)

    return facts


# Execute the program
print("Initial Facts:")
for fact in sorted(facts):
    print(fact)

print("\nForward Chaining Process:")
result = forward_chaining(facts, rules)

print("\nFinal Result:")
if ("Criminal", "Robert") in result:
    print("Robert is a Criminal")
else:
    print("Robert is not proved to be a Criminal")
