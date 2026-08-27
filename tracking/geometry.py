"""Geometry utilities for the Air Aegis simulation."""

import math

from tracking.track import Track


def horizontal_distance(
    first: Track,
    second: Track,
) -> float:
    """Calculate horizontal distance between two tracks."""
    dx = first.x - second.x
    dy = first.y - second.y

    return math.hypot(dx, dy)


def altitude_difference(
    first: Track,
    second: Track,
) -> float:
    """Calculate absolute altitude difference between two tracks."""
    return abs(first.altitude - second.altitude)


def speed_magnitude(
    velocity_x: float,
    velocity_y: float,
    velocity_z: float = 0.0,
) -> float:
    """Calculate 3D velocity magnitude."""
    import math

    return math.sqrt(
        velocity_x ** 2
        + velocity_y ** 2
        + velocity_z ** 2
    )


def ground_speed(
    velocity_x: float,
    velocity_y: float,
) -> float:
    """Calculate horizontal speed magnitude."""
    import math

    return math.hypot(velocity_x, velocity_y)


def spatial_distance(
    first: Track,
    second: Track,
) -> float:
    """Calculate 3D distance between two tracks."""
    dx = first.x - second.x
    dy = first.y - second.y
    dz = first.altitude - second.altitude

    return (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5


def heading_degrees(
    velocity_x: float,
    velocity_y: float,
) -> float:
    """Calculate horizontal heading in degrees."""
    import math

    if velocity_x == 0 and velocity_y == 0:
        return 0.0

    return math.degrees(math.atan2(velocity_y, velocity_x)) % 360.0
