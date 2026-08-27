from simulation.world import create_demo_object
from sensors.simulator import SimulatedSensor


def test_sensor_produces_observation():
    sensor = SimulatedSensor("SENSOR-01", random_seed=42)
    obj = create_demo_object()

    observation = sensor.observe(obj)

    assert observation.sensor_id == "SENSOR-01"
    assert observation.object_id == obj.object_id
    assert isinstance(observation.x, float)
    assert isinstance(observation.y, float)
    assert isinstance(observation.altitude, float)
    assert 0.0 < observation.confidence <= 1.0


def test_sensor_is_reproducible_with_fixed_seed():
    obj = create_demo_object()

    sensor_1 = SimulatedSensor("SENSOR-01", random_seed=7)
    sensor_2 = SimulatedSensor("SENSOR-01", random_seed=7)

    observation_1 = sensor_1.observe(obj)
    observation_2 = sensor_2.observe(obj)

    assert observation_1 == observation_2


def test_sensor_rejects_invalid_noise():
    try:
        SimulatedSensor("SENSOR-01", position_noise=-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative noise should raise ValueError")
