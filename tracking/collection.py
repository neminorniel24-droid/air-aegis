"""Track collection serialization for Air Aegis."""

from tracking.manager import TrackManager
from tracking.snapshot import track_to_dict


def tracks_to_dict(manager: TrackManager) -> list[dict]:
    """Convert all active tracks into dictionaries."""
    return [track_to_dict(track) for track in manager.all()]
