from math import sqrt
import matplotlib.pyplot as plt
from typing import Tuple, List
import random
from tqdm.auto import tqdm
import multiprocessing
from shapes import shapes

# golden ratio
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

def jump(p1: Tuple, p2: Tuple, jump_distance: float = 1/2) -> Tuple:
    x = p1[0] + (p2[0] - p1[0]) * jump_distance
    y = p1[1] + (p2[1] - p1[1]) * jump_distance
    return (x, y)

def get_vertex(shape: List[Tuple], prev_vertex: Tuple | None = None) -> Tuple:
    if prev_vertex is None:
        return random.choice(shape)
    else:
        # choose a random vertex that is not the previous vertex
        vertex = random.choice(shape)
        while vertex == prev_vertex:
            vertex = random.choice(shape)
        return vertex

def draw_shape(shape_name: str, iterations: int = 10000, marker_size: float = 0.05, color_points: bool = False, tid: int = 0) -> None:
    try:
        shape = shapes[shape_name]
    except KeyError:
        raise ValueError(f"shape_name must be one of {list(shapes.keys())}")

    # create plot
    fig, ax = plt.subplots()

    # plot the triangle with a solid line connecting the points
    ax.plot(
        [p[0] for p in shape] + [shape[0][0]],
        [p[1] for p in shape] + [shape[0][1]],
        "r-",
    )

    ax.set_aspect("equal")
    ax.set_axis_off()

    current_point = (0, 0)
    random_point = None
    for _ in tqdm(range(iterations), desc=f"{shape_name}-{iterations}-{marker_size}", position=tid):
        # pick a random point from the triangle
        random_point = get_vertex(shape, None)
        # find the midpoint between the current point and the random point
        current_point = jump(current_point, random_point, jump_distance=PHI_INV)
        # plot the current point
        ax.plot(current_point[0], current_point[1], random_point[2] if color_points else "k.", markersize=marker_size)
    plt.savefig(f"images/{shape_name}-{iterations}-{marker_size}.png")
    plt.close()

SHAPES_TO_DRAW = [
    ("isosceles_triangle", 500000, 0.05, False),
    ("quadrilateral", 200000, 0.05, False),
    ("dome_thing", 200000, 0.05, False),
    ("dented_dome", 200000, 0.05, False),
    ("hexagon", 400000, 0.05, False),
]

# create a new list of shapes to draw with a tid as the last element in the tuple
TID_SHAPES_TO_DRAW = [(shape_name, iterations, marker_size, color_points, tid) for tid, (shape_name, iterations, marker_size, color_points) in enumerate(SHAPES_TO_DRAW)]



with multiprocessing.Pool() as pool:
    pool.starmap(draw_shape, TID_SHAPES_TO_DRAW)

        