"""Synthetic sensor model for Air Aegis."""

from dataclasses import dataclass
import numpy as np

from simulation.world import SimulatedObject


@dataclass
class SensorObservation:
    """A noisy observation produced by a simulated sensor."""

    sensor_id: str
    object_id: str
    x: float
    y: float
    altitude: float
    confidence: float


class SimulatedSensor:
    """Generate noisy observations from simulated airborne objects."""

    def __init__(
        self,
        sensor_id: str,
        position_noise: float = 5.0,
        altitude_noise: float = 2.0,
        random_seed: int = 42,
    ) -> None:
        if not sensor_id.strip():
            raise ValueError("sensor_id must not be empty.")

        if position_noise < 0 or altitude_noise < 0:
            raise ValueError("noise values must not be negative.")

        self.sensor_id = sensor_id
        self.position_noise = position_noise
        self.altitude_noise = altitude_noise
        self.rng = np.random.default_rng(random_seed)

    def observe(self, obj: SimulatedObject) -> SensorObservation:
        """Create a noisy observation of a simulated object."""
        x = obj.x + self.rng.normal(0, self.position_noise)
        y = obj.y + self.rng.normal(0, self.position_noise)
        altitude = obj.altitude + self.rng.normal(0, self.altitude_noise)

        noise = self.position_noise + self.altitude_noise
        confidence = 1.0 / (1.0 + noise)

        return SensorObservation(
            sensor_id=self.sensor_id,
            object_id=obj.object_id,
            x=float(x),
            y=float(y),
            altitude=float(altitude),
            confidence=float(confidence),
        )
