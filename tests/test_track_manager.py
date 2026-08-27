import pytest

from tracking.manager import TrackManager
from tracking.track import Track


def make_track(object_id: str) -> Track:
    return Track(
        object_id=object_id,
        x=0.0,
        y=0.0,
        altitude=1000.0,
        confidence=0.8,
    )


def test_manager_adds_track():
    manager = TrackManager()
    track = make_track("OBJ-001")

    manager.add(track)

    assert len(manager) == 1
    assert manager.get("OBJ-001") is track


def test_manager_rejects_duplicate_track():
    manager = TrackManager()
    track = make_track("OBJ-001")

    manager.add(track)

    with pytest.raises(ValueError, match="already exists"):
        manager.add(make_track("OBJ-001"))


def test_manager_updates_existing_track():
    manager = TrackManager()
    manager.add(make_track("OBJ-001"))

    updated = manager.update(
        "OBJ-001",
        x=50.0,
        y=25.0,
        altitude=1200.0,
        confidence=0.9,
    )

    assert updated.x == 50.0
    assert updated.y == 25.0
    assert updated.altitude == 1200.0
    assert updated.confidence == 0.9
    assert updated.observation_count == 1


def test_manager_rejects_unknown_track_update():
    manager = TrackManager()

    with pytest.raises(KeyError, match="Unknown track"):
        manager.update(
            "UNKNOWN",
            x=0.0,
            y=0.0,
            altitude=1000.0,
            confidence=0.5,
        )


def test_manager_returns_all_tracks():
    manager = TrackManager()
    manager.add(make_track("OBJ-001"))
    manager.add(make_track("OBJ-002"))

    tracks = manager.all()

    assert len(tracks) == 2
    assert {track.object_id for track in tracks} == {
        "OBJ-001",
        "OBJ-002",
    }


def test_manager_removes_track():
    manager = TrackManager()
    track = make_track("OBJ-REMOVE")

    manager.add(track)
    removed = manager.remove("OBJ-REMOVE")

    assert removed is track
    assert manager.get("OBJ-REMOVE") is None
    assert len(manager) == 0


def test_manager_remove_unknown_returns_none():
    manager = TrackManager()

    assert manager.remove("UNKNOWN") is None
