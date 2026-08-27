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
    velocity_x: float = 0.0
    velocity_y: float = 0.0
    velocity_z: float = 0.0

    def update(
        self,
        x: float,
        y: float,
        altitude: float,
        confidence: float,
        velocity_x: float | None = None,
        velocity_y: float | None = None,
        velocity_z: float | None = None,
    ) -> None:
        """Update the track with a new estimated state."""
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1.")

        self.x = float(x)
        self.y = float(y)
        self.altitude = float(altitude)
        self.confidence = float(confidence)

        if velocity_x is not None:
            self.velocity_x = float(velocity_x)

        if velocity_y is not None:
            self.velocity_y = float(velocity_y)

        if velocity_z is not None:
            self.velocity_z = float(velocity_z)

        self.observation_count += 1
