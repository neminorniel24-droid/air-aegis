"""Track representation for the Air Aegis simulation."""

from dataclasses import dataclass


@dataclass
class Track:
    """Current state estimate for a simulated airborne object."""

    object_id: str
    x: float
    y: float
    altitude: float
    confidence: float
    observation_count: int = 0

    def update(
        self,
        x: float,
        y: float,
        altitude: float,
        confidence: float,
    ) -> None:
        """Update the track with a new estimated state."""
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1.")

        self.x = float(x)
        self.y = float(y)
        self.altitude = float(altitude)
        self.confidence = float(confidence)
        self.observation_count += 1
