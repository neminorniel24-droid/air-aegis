from sensors.network import SensorNetwork
from sensors.simulator import SimulatedSensor
from simulation.world import create_demo_object


def test_sensor_network_collects_multiple_observations():
    sensors = [
        SimulatedSensor("SENSOR-01", random_seed=1),
        SimulatedSensor("SENSOR-02", random_seed=2),
        SimulatedSensor("SENSOR-03", random_seed=3),
    ]

    network = SensorNetwork(sensors)
    observations = network.observe(create_demo_object())

    assert len(observations) == 3
    assert [obs.sensor_id for obs in observations] == [
        "SENSOR-01",
        "SENSOR-02",
        "SENSOR-03",
    ]


def test_sensor_network_preserves_object_identity():
    obj = create_demo_object()

    network = SensorNetwork(
        [SimulatedSensor("SENSOR-01", random_seed=42)]
    )

    observations = network.observe(obj)

    assert observations[0].object_id == obj.object_id


def test_sensor_network_rejects_empty_sensor_list():
    try:
        SensorNetwork([])
    except ValueError:
        pass
    else:
        raise AssertionError("Empty sensor list should raise ValueError")
