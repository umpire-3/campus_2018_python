import random
import map_generator


world_size = 0
world = None


def print_world(player_pos):
    print('You at: {}'.format(player_pos))
    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            if player_pos[0] == x and player_pos[1] == y:
                print('Player ', end='')
            else:
                print('{} '.format(cell), end='')
        print()


def get_neighbor_cells(player_pos):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx, dy) != (0, 0):
                neighbor_pos = [player_pos[0] + dx, player_pos[1] + dy]
                if is_inside_world(neighbor_pos):
                    neighbors.append(neighbor_pos)
    return neighbors


def is_trap_around(player_pos):
    neighbors = get_neighbor_cells(player_pos)
    is_trap_around = any(world[neighbor[1]][neighbor[0]] == 'Trap' for neighbor in neighbors)
    return is_trap_around


def is_treasure_around(player_pos):
    neighbors = get_neighbor_cells(player_pos)
    is_treasure_around = any(world[neighbor[1]][neighbor[0]] == 'Treasure' for neighbor in neighbors)
    return is_treasure_around


def is_trapped(player_pos):
    return world[player_pos[1]][player_pos[0]] == 'Trap'


def is_found_treasure(player_pos):
    return world[player_pos[1]][player_pos[0]] == 'Treasure'


def is_inside_world(pos):
    return all(0 <= coord < len(world) for coord in pos)


def move_player(player_pos, direction):
    # new_pos = [c0 + c1 for c0, c1 in zip(player_pos, direction)]
    new_pos = [
        player_pos[0] + direction[0],
        player_pos[1] + direction[1]
    ]
    if is_inside_world(new_pos):
        player_pos[:] = new_pos


def create_world(size):
    global world_size
    global world

    world_size = size
    world = map_generator.generate(size)


def spawn_player():
    player_pos = [random.choice(range(world_size)), random.choice(range(world_size))]

    while world[player_pos[1]][player_pos[0]] is not None:
        player_pos = [random.choice(range(world_size)), random.choice(range(world_size))]

    return player_pos