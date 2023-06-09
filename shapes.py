from math import sqrt, cos, sin, pi

shapes = {
    "equilateral_triangle": [
        (0, 0, "g."),
        (-0.5, -sqrt(3) / 2, "r."),
        (0.5, -sqrt(3) / 2, "b."),
    ],
    "isosceles_triangle": [
        (0.3, 0.5, "g."),
        (0, 0, "r."),
        (1, 0, "b."),
    ],
    "square": [
        (0, 0, "g."),
        (1, 0, "r."),
        (1, 1, "b."),
        (0, 1, "y."),
    ],
    "dented_square": [
        (0, 0, "g."),
        (1, 0, "r."),
        (1, 1, "b."),
        (0.5, 0.5, "y."),
        (0, 1, "c."),
    ],
    "slightly_dented_square": [
        (0, 0, "g."),
        (1, 0, "r."),
        (1, 1, "b."),
        (0.5, 0.75, "y."),
        (0, 1, "c."),
    ],
    "four_star": [
        (0, 0, "g."),
        (0.5, 0.25, "r."),
        (1, 0, "b."),
        (0.75, 0.5, "y."),
        (1, 1, "c."),
        (0.5, 0.75, "m."),
        (0, 1, "k."),
        (0.25, 0.5, "w."),
    ],
    "quadrilateral": [
        (0, 0, "g."),
        (0, 1, "r."),
        (0.75, 0.6, "b."),
        (1, 0, "y."),
    ],
    "dome_thing": [
        (0, 0, "g."),
        (1, 0, "r."),
        (0.75, 0.6, "b."),
        (0.5, 0.7, "y."),
        (0.2, 0.4, "c."),
    ],
    "dented_dome": [
        (0, 0, "g."),
        (1, 0, "r."),
        (0.4, 0.4, "b."),
        (0.5, 0.7, "y."),
        (0.2, 0.4, "c."),
    ],
    "pentagon": [
        (0, 1, "g."),
        (cos(pi / 10), sin(pi / 10), "r."),
        (cos(3 * pi / 10), -sin(3 * pi / 10), "b."),
        (-cos(3 * pi / 10), -sin(3 * pi / 10), "y."),
        (-cos(pi / 10), sin(pi / 10), "c."),
    ],
    "hexagon": [
        (1, 0, "g."),
        (0.5, sqrt(3) / 2, "r."),
        (-0.5, sqrt(3) / 2, "b."),
        (-1, 0, "y."),
        (-0.5, -sqrt(3) / 2, "c."),
        (0.5, -sqrt(3) / 2, "m."),
    ],
}
