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
    age_seconds: float = 0.0
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


    def summary(self) -> dict:
        """Return a compact representation of the current track state."""
        return {
            "object_id": self.object_id,
            "position": {
                "x": self.x,
                "y": self.y,
                "altitude": self.altitude,
            },
            "velocity": {
                "x": self.velocity_x,
                "y": self.velocity_y,
                "z": self.velocity_z,
            },
            "confidence": self.confidence,
            "observation_count": self.observation_count,
        }

    def advance_age(self, dt: float) -> None:
        """Advance the time since the track was created."""
        if dt < 0:
            raise ValueError("dt must not be negative.")

        self.age_seconds += float(dt)

    def status(self) -> str:
        """Return a human-readable confidence status."""
        if self.confidence >= 0.8:
            return "High confidence"
        if self.confidence >= 0.5:
            return "Medium confidence"
        return "Low confidence"
