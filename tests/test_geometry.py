from tracking.geometry import altitude_difference, horizontal_distance
from tracking.track import Track


def make_track(
    object_id: str,
    x: float,
    y: float,
    altitude: float,
) -> Track:
    return Track(
        object_id=object_id,
        x=x,
        y=y,
        altitude=altitude,
        confidence=0.8,
    )


def test_horizontal_distance():
    first = make_track("A", 0.0, 0.0, 1000.0)
    second = make_track("B", 3.0, 4.0, 1000.0)

    assert horizontal_distance(first, second) == 5.0


def test_horizontal_distance_same_position():
    first = make_track("A", 10.0, 20.0, 1000.0)
    second = make_track("B", 10.0, 20.0, 1200.0)

    assert horizontal_distance(first, second) == 0.0


def test_altitude_difference():
    first = make_track("A", 0.0, 0.0, 1000.0)
    second = make_track("B", 0.0, 0.0, 1350.0)

    assert altitude_difference(first, second) == 350.0


def test_speed_magnitude():
    from tracking.geometry import speed_magnitude

    assert speed_magnitude(3.0, 4.0) == 5.0


def test_speed_magnitude_supports_vertical_velocity():
    from tracking.geometry import speed_magnitude

    assert speed_magnitude(2.0, 3.0, 6.0) == 7.0


def test_ground_speed():
    from tracking.geometry import ground_speed

    assert ground_speed(3.0, 4.0) == 5.0


def test_ground_speed_zero():
    from tracking.geometry import ground_speed

    assert ground_speed(0.0, 0.0) == 0.0


def test_spatial_distance():
    from tracking.geometry import spatial_distance

    first = make_track("A", 0.0, 0.0, 0.0)
    second = make_track("B", 3.0, 4.0, 12.0)

    assert spatial_distance(first, second) == 13.0


def test_heading_degrees():
    from tracking.geometry import heading_degrees

    assert heading_degrees(1.0, 0.0) == 0.0
    assert heading_degrees(0.0, 1.0) == 90.0
    assert heading_degrees(-1.0, 0.0) == 180.0


def test_heading_degrees_for_stationary_object():
    from tracking.geometry import heading_degrees

    assert heading_degrees(0.0, 0.0) == 0.0
