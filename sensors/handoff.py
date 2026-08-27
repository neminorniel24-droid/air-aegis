"""Sensor handoff simulation for Air Aegis."""

from dataclasses import dataclass

from sensors.simulator import SensorObservation
from tracking.track import Track


@dataclass
class HandoffEvent:
    """Record a track handoff between two sensors."""

    object_id: str
    source_sensor: str
    target_sensor: str


def create_handoff(
    observation: SensorObservation,
    target_sensor: str,
) -> HandoffEvent:
    """Create a handoff event from the current observing sensor."""
    if not target_sensor.strip():
        raise ValueError("target_sensor must not be empty.")

    if observation.sensor_id == target_sensor:
        raise ValueError("target_sensor must differ from source sensor.")

    return HandoffEvent(
        object_id=observation.object_id,
        source_sensor=observation.sensor_id,
        target_sensor=target_sensor,
    )
