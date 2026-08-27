import json

from tracking.snapshot import track_to_dict, track_to_json
from tracking.track import Track


def test_track_to_dict():
    track = Track(
        object_id="OBJ-001",
        x=10.0,
        y=20.0,
        altitude=1000.0,
        confidence=0.8,
    )

    result = track_to_dict(track)

    assert result["object_id"] == "OBJ-001"
    assert result["x"] == 10.0
    assert result["altitude"] == 1000.0


def test_track_to_json_is_valid_json():
    track = Track(
        object_id="OBJ-002",
        x=5.0,
        y=15.0,
        altitude=1200.0,
        confidence=0.9,
    )

    result = track_to_json(track)
    decoded = json.loads(result)

    assert decoded["object_id"] == "OBJ-002"
    assert decoded["confidence"] == 0.9
