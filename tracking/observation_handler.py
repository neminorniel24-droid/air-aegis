"""Convert sensor observations into track updates."""

from sensors.simulator import SensorObservation
from tracking.manager import TrackManager
from tracking.track import Track


def process_observation(
    manager: TrackManager,
    observation: SensorObservation,
) -> Track:
    """Create or update a track from a sensor observation."""
    track = manager.get(observation.object_id)

    if track is None:
        track = Track(
            object_id=observation.object_id,
            x=observation.x,
            y=observation.y,
            altitude=observation.altitude,
            confidence=observation.confidence,
            observation_count=1,
        )
        manager.add(track)
        return track

    return manager.update(
        object_id=observation.object_id,
        x=observation.x,
        y=observation.y,
        altitude=observation.altitude,
        confidence=observation.confidence,
    )
