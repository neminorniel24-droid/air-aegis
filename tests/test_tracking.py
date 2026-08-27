import pytest

from tracking.track import Track


def test_track_initial_state():
    track = Track(
        object_id="OBJ-001",
        x=10.0,
        y=20.0,
        altitude=1000.0,
        confidence=0.8,
    )

    assert track.object_id == "OBJ-001"
    assert track.x == 10.0
    assert track.y == 20.0
    assert track.altitude == 1000.0
    assert track.confidence == 0.8
    assert track.observation_count == 0


def test_track_update_changes_state():
    track = Track(
        object_id="OBJ-001",
        x=0.0,
        y=0.0,
        altitude=1000.0,
        confidence=0.5,
    )

    track.update(
        x=25.0,
        y=30.0,
        altitude=1100.0,
        confidence=0.9,
    )

    assert track.x == 25.0
    assert track.y == 30.0
    assert track.altitude == 1100.0
    assert track.confidence == 0.9
    assert track.observation_count == 1


def test_track_rejects_invalid_confidence():
    track = Track(
        object_id="OBJ-001",
        x=0.0,
        y=0.0,
        altitude=1000.0,
        confidence=0.5,
    )

    with pytest.raises(ValueError, match="confidence"):
        track.update(
            x=0.0,
            y=0.0,
            altitude=1000.0,
            confidence=1.5,
        )
