from tracking.collection import tracks_to_dict
from tracking.manager import TrackManager
from tracking.track import Track


def test_tracks_to_dict_returns_all_tracks():
    manager = TrackManager()

    manager.add(
        Track(
            object_id="OBJ-001",
            x=1.0,
            y=2.0,
            altitude=1000.0,
            confidence=0.8,
        )
    )

    manager.add(
        Track(
            object_id="OBJ-002",
            x=3.0,
            y=4.0,
            altitude=1200.0,
            confidence=0.9,
        )
    )

    result = tracks_to_dict(manager)

    assert len(result) == 2
    assert {item["object_id"] for item in result} == {
        "OBJ-001",
        "OBJ-002",
    }
