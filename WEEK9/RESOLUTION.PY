
print("PROOF BY RESOLUTION")

print("\nStep 1: Given Facts")
print("C1: Alive(Anil)")
print("C2: Eats(Anil, Peanuts)")

print("\nStep 2: Convert Rules into CNF")
print("C3: ~Alive(x) OR ~Killed(x)")
print("C4: ~Eats(y,z) OR Killed(y) OR Food(z)")
print("C5: ~Food(x) OR Likes(John,x)")

print("\nStep 3: Negate the Goal")
print("C6: ~Likes(John, Peanuts)")

print("\nStep 4: Apply Resolution")
print("C1 + C3")
print("Resolvent: ~Killed(Anil)")

print("\nStep 5: Resolve C4")
print("~Eats(Anil,Peanuts) OR Killed(Anil) OR Food(Peanuts)")
print("Resolving with ~Killed(Anil)")
print("Resolvent: ~Eats(Anil,Peanuts) OR Food(Peanuts)")

print("\nStep 6: Resolve with C2")
print("Eats(Anil, Peanuts)")
print("Resolvent: Food(Peanuts)")

print("\nStep 7: Resolve with C5")
print("~Food(Peanuts) OR Likes(John,Peanuts)")
print("Resolvent: Likes(John,Peanuts)")

print("\nStep 8: Resolve with Negated Goal")
print("Likes(John,Peanuts)")
print("~Likes(John,Peanuts)")
print("Resolvent: NIL (Empty Clause)")

print("\nConclusion:")
print("John likes Peanuts is PROVED.")
