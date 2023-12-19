with open("input.txt") as f:
    pipe_map = f.read().splitlines()

# Find the starting point
for i, pipe_row in enumerate(pipe_map):
    for j, pipe in enumerate(pipe_row):
        if pipe == "S":
            start_coords = (i, j)

# Get map dimensions
pipe_map_width = len(pipe_map[0])
pipe_map_height = len(pipe_map)


# Convert coordinates to a key
def coord_to_key(coord):
    return f"{coord[0]}-{coord[1]}"


# Convert a key to coordinates
def key_to_coord(key):
    return tuple(map(int, key.split("-")))


# Get the possible directions for a given pipe
def get_possible_directions(pipe):
    possible_direction_map = {
        "|": ["N", "S"],
        "-": ["E", "W"],
        "L": ["N", "E"],
        "J": ["N", "W"],
        "7": ["S", "W"],
        "F": ["S", "E"],
        ".": [],
        "S": ["N", "E", "S", "W"],
    }

    return possible_direction_map.get(pipe)


# Determine if the next direction is valid
def is_next_direction_valid(pipe, direction):
    next_direction_map = {
        "N": ["|", "7", "F"],
        "E": ["-", "7", "J"],
        "S": ["|", "L", "J"],
        "W": ["-", "L", "F"],
    }

    return pipe in next_direction_map.get(direction)


# Get the next coordinate
def get_next_coord(coord, direction):
    pipe_x, pipe_y = coord

    next_coord_map = {
        "N": (pipe_x - 1, pipe_y),
        "E": (pipe_x, pipe_y + 1),
        "S": (pipe_x + 1, pipe_y),
        "W": (pipe_x, pipe_y - 1),
    }

    return next_coord_map[direction]


visited_coords = {}


def iterate_over_pipes(coord, prev_direction, distance):
    pipe_x, pipe_y = coord
    pipe = pipe_map[pipe_x][pipe_y]

    # Update the visited coords
    visited_coords[coord_to_key(coord)] = min(
        distance, visited_coords.get(coord_to_key(coord), float("inf"))
    )

    valid_next_steps = []

    for next_direction in get_possible_directions(pipe):
        # Skip if we're going back the way we came
        opposite_direction_map = {"N": "S", "E": "W", "S": "N", "W": "E"}
        if next_direction == opposite_direction_map.get(prev_direction):
            continue

        next_coord = get_next_coord(coord, next_direction)
        next_pipe_x, next_pipe_y = next_coord

        # Skip if we're going off the map
        if (
            next_pipe_x < 0
            or next_coord[0] >= pipe_map_width
            or next_pipe_y < 0
            or next_coord[1] >= pipe_map_height
        ):
            continue

        next_pipe = pipe_map[next_pipe_x][next_pipe_y]

        # Skip if the next direction is invalid
        if not is_next_direction_valid(next_pipe, next_direction):
            continue

        # Skip if next coord has a smaller distance than the current distance
        if visited_coords.get(coord_to_key(next_coord), float("inf")) <= distance:
            continue

        # If we've reached this point, the next direction is valid
        valid_next_steps.append((next_coord, next_direction))

    # If there's no valid next step return the distance
    if len(valid_next_steps) == 0:
        return

    # Otherwise, iterate over the valid next steps
    for next_coord, next_direction in valid_next_steps:
        iterate_over_pipes(next_coord, next_direction, distance + 1)


# Set the max recursion depth
import sys
sys.setrecursionlimit(100000)

# Start the iteration
iterate_over_pipes(start_coords, None, 0)

# Get the max distance
max_distance = max(visited_coords.values())
print("Max distance:", max_distance)
