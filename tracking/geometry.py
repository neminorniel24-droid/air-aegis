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
