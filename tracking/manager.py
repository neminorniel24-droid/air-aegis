"""Track management for the Air Aegis simulation."""

from tracking.track import Track


class TrackManager:
    """Maintain and update multiple airborne-object tracks."""

    def __init__(self) -> None:
        self._tracks: dict[str, Track] = {}

    def add(self, track: Track) -> None:
        """Add a new track."""
        if track.object_id in self._tracks:
            raise ValueError(
                f"Track already exists: {track.object_id}"
            )

        self._tracks[track.object_id] = track

    def get(self, object_id: str) -> Track | None:
        """Return a track by object ID."""
        return self._tracks.get(object_id)

    def update(
        self,
        object_id: str,
        x: float,
        y: float,
        altitude: float,
        confidence: float,
    ) -> Track:
        """Update an existing track."""
        track = self.get(object_id)

        if track is None:
            raise KeyError(f"Unknown track: {object_id}")

        track.update(
            x=x,
            y=y,
            altitude=altitude,
            confidence=confidence,
        )

        return track

    def all(self) -> list[Track]:
        """Return all active tracks."""
        return list(self._tracks.values())

    def __len__(self) -> int:
        """Return the number of active tracks."""
        return len(self._tracks)
