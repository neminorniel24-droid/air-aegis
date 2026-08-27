import pytest

from sensors.handoff import create_handoff
from sensors.simulator import SimulatedSensor
from simulation.world import create_demo_object


def test_handoff_preserves_object_identity():
    obj = create_demo_object()
    sensor = SimulatedSensor("SENSOR-01", random_seed=42)
    observation = sensor.observe(obj)

    event = create_handoff(
        observation,
        "SENSOR-02",
    )

    assert event.object_id == obj.object_id
    assert event.source_sensor == "SENSOR-01"
    assert event.target_sensor == "SENSOR-02"


def test_handoff_requires_different_target_sensor():
    obj = create_demo_object()
    sensor = SimulatedSensor("SENSOR-01", random_seed=42)
    observation = sensor.observe(obj)

    with pytest.raises(ValueError, match="differ"):
        create_handoff(
            observation,
            "SENSOR-01",
        )


def test_handoff_requires_target_sensor():
    obj = create_demo_object()
    sensor = SimulatedSensor("SENSOR-01", random_seed=42)
    observation = sensor.observe(obj)

    with pytest.raises(ValueError, match="must not be empty"):
        create_handoff(observation, "")
