from simulation.world import advance_object, create_demo_object


def test_demo_object_has_expected_initial_state():
    obj = create_demo_object()

    assert obj.object_id == "OBJ-001"
    assert obj.x == 0.0
    assert obj.y == 0.0
    assert obj.altitude == 1000.0
    assert obj.speed == 120.0


def test_object_advances_with_time():
    obj = create_demo_object()

    moved = advance_object(obj, 2.0)

    assert moved.x == 240.0
    assert moved.y == 0.0
    assert moved.altitude == obj.altitude


def test_negative_time_is_rejected():
    obj = create_demo_object()

    try:
        advance_object(obj, -1.0)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative time should raise ValueError")
