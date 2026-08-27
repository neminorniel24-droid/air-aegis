"""Serializable track snapshots for Air Aegis."""

from dataclasses import asdict
import json

from tracking.track import Track


def track_to_dict(track: Track) -> dict:
    """Convert a track to a plain dictionary."""
    return asdict(track)


def track_to_json(track: Track) -> str:
    """Serialize a track to readable JSON."""
    return json.dumps(track_to_dict(track), indent=2)
