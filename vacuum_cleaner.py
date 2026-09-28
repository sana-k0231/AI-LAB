print("SANA KISHOR 1BF24CS270")
def simple_reflex_agent(room_a, room_b, position):

    print("\n--- Simple Reflex Agent ---")

    while True:

        print("Vacuum is in Room", position)

        # Current room is dirty
        if position == 'A' and room_a == 'Dirty':
            print("Room A is Dirty -> Suck")
            room_a = 'Clean'

        elif position == 'B' and room_b == 'Dirty':
            print("Room B is Dirty -> Suck")
            room_b = 'Clean'

        # Current room is clean, move to other room
        elif position == 'A' and room_a == 'Clean':
            print("Room A is Clean -> Move Right")
            position = 'B'

        elif position == 'B' and room_b == 'Clean':
            print("Room B is Clean -> Move Left")
            position = 'A'

        # Both rooms clean
        if room_a == 'Clean' and room_b == 'Clean':
            print("Both rooms are Clean")
            break

    return room_a, room_b, position


# Goal Based Agent
def goal_based_agent(room_a, room_b, position):

    print("\n--- Goal Based Agent ---")

    while room_a != 'Clean' or room_b != 'Clean':

        print("Vacuum is in Room", position)

        # Current room is dirty
        if position == 'A' and room_a == 'Dirty':
            print("Room A is Dirty -> Suck")
            room_a = 'Clean'

        elif position == 'B' and room_b == 'Dirty':
            print("Room B is Dirty -> Suck")
            room_b = 'Clean'

        # Current room is clean and other room is dirty
        elif position == 'A' and room_a == 'Clean' and room_b == 'Dirty':
            print("Room A is Clean, Room B is Dirty -> Move Right")
            position = 'B'

        elif position == 'B' and room_b == 'Clean' and room_a == 'Dirty':
            print("Room B is Clean, Room A is Dirty -> Move Left")
            position = 'A'

    print("Goal Achieved: Both rooms are Clean")


# Main program
print("VACUUM CLEANER")

room_a = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_b = input("Enter status of Room B (Clean/Dirty): ").capitalize()

position = input("Enter initial vacuum location (A/B): ").upper()

print("\nInitial Room A:", room_a)
print("Initial Room B:", room_b)
print("Initial Vacuum Location: Room", position)

# Run Simple Reflex Agent
simple_reflex_agent(room_a, room_b, position)

# Run Goal Based Agent
goal_based_agent(room_a, room_b, position)