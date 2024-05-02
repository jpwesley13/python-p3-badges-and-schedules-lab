def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    batch = []
    for name in names:
        batch.append(f'Hello, my name is {name}.')
    return batch

def assign_rooms(names):
    room_assignment = []
    for n in range(8):
        room_assignment.append(f"Hello, {names[n]}! You'll be assigned to room {n+1}!")
    return room_assignment

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
