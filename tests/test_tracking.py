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


def test_track_stores_velocity():
    track = Track(
        object_id="OBJ-002",
        x=0.0,
        y=0.0,
        altitude=1000.0,
        confidence=0.8,
        velocity_x=120.0,
        velocity_y=5.0,
    )

    assert track.velocity_x == 120.0
    assert track.velocity_y == 5.0


def test_track_update_can_update_velocity():
    track = Track(
        object_id="OBJ-003",
        x=0.0,
        y=0.0,
        altitude=1000.0,
        confidence=0.8,
    )

    track.update(
        x=10.0,
        y=20.0,
        altitude=1050.0,
        confidence=0.9,
        velocity_x=50.0,
        velocity_y=7.5,
    )

    assert track.velocity_x == 50.0
    assert track.velocity_y == 7.5


def test_track_stores_vertical_velocity():
    track = Track(
        object_id="OBJ-004",
        x=0.0,
        y=0.0,
        altitude=1000.0,
        confidence=0.8,
        velocity_z=25.0,
    )

    assert track.velocity_z == 25.0


def test_track_update_can_change_vertical_velocity():
    track = Track(
        object_id="OBJ-005",
        x=0.0,
        y=0.0,
        altitude=1000.0,
        confidence=0.8,
    )

    track.update(
        x=10.0,
        y=20.0,
        altitude=1100.0,
        confidence=0.9,
        velocity_z=30.0,
    )

    assert track.velocity_z == 30.0


def test_track_summary_contains_current_state():
    track = Track(
        object_id="OBJ-006",
        x=10.0,
        y=20.0,
        altitude=1500.0,
        confidence=0.85,
        velocity_x=40.0,
        velocity_y=5.0,
        velocity_z=3.0,
        observation_count=2,
    )

    summary = track.summary()

    assert summary["object_id"] == "OBJ-006"
    assert summary["position"]["altitude"] == 1500.0
    assert summary["velocity"]["x"] == 40.0
    assert summary["velocity"]["z"] == 3.0
    assert summary["confidence"] == 0.85
    assert summary["observation_count"] == 2


def test_track_status_classification():
    high = Track("HIGH", 0, 0, 1000, 0.9)
    medium = Track("MEDIUM", 0, 0, 1000, 0.6)
    low = Track("LOW", 0, 0, 1000, 0.2)

    assert high.status() == "High confidence"
    assert medium.status() == "Medium confidence"
    assert low.status() == "Low confidence"


def test_track_status_classification():
    high = Track("HIGH", 0, 0, 1000, 0.9)
    medium = Track("MEDIUM", 0, 0, 1000, 0.6)
    low = Track("LOW", 0, 0, 1000, 0.2)

    assert high.status() == "High confidence"
    assert medium.status() == "Medium confidence"
    assert low.status() == "Low confidence"


def test_track_age_advances():
    track = Track("OBJ-AGE", 0, 0, 1000, 0.8)

    track.advance_age(2.5)

    assert track.age_seconds == 2.5


def test_track_age_rejects_negative_time():
    track = Track("OBJ-AGE-NEG", 0, 0, 1000, 0.8)

    try:
        track.advance_age(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative time should raise ValueError")


def test_track_last_seen_updates_on_observation():
    track = Track("OBJ-SEEN", 0, 0, 1000, 0.8)

    track.advance_age(3.0)

    track.update(
        x=5,
        y=6,
        altitude=1100,
        confidence=0.9,
    )

    assert track.last_seen == 3.0


def test_track_freshness():
    track = Track("OBJ-FRESH", 0, 0, 1000, 0.8)

    track.update(
        x=1,
        y=1,
        altitude=1000,
        confidence=0.8,
    )

    track.advance_age(2.0)

    assert track.is_fresh(max_age=5.0)
    assert not track.is_fresh(max_age=1.0)
