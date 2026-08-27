"""Distributed sensor network simulation for Air Aegis."""

from sensors.simulator import SensorObservation, SimulatedSensor
from simulation.world import SimulatedObject


class SensorNetwork:
    """Collect observations from multiple simulated sensors."""

    def __init__(self, sensors: list[SimulatedSensor]) -> None:
        if not sensors:
            raise ValueError("sensors must not be empty.")

        self.sensors = sensors

    def observe(self, obj: SimulatedObject) -> list[SensorObservation]:
        """Collect observations from every sensor."""
        return [sensor.observe(obj) for sensor in self.sensors]
