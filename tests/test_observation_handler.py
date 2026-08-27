from sensors.simulator import SimulatedSensor
from simulation.world import create_demo_object
from tracking.manager import TrackManager
from tracking.observation_handler import process_observation


def test_first_observation_creates_track():
    obj = create_demo_object()
    sensor = SimulatedSensor("SENSOR-01", random_seed=42)
    observation = sensor.observe(obj)

    manager = TrackManager()
    track = process_observation(manager, observation)

    assert track.object_id == obj.object_id
    assert len(manager) == 1
    assert track.observation_count == 1


def test_second_observation_updates_existing_track():
    obj = create_demo_object()
    sensor = SimulatedSensor("SENSOR-01", random_seed=42)

    manager = TrackManager()

    first = sensor.observe(obj)
    second = sensor.observe(obj)

    process_observation(manager, first)
    track = process_observation(manager, second)

    assert len(manager) == 1
    assert track.observation_count == 2
    assert track.object_id == obj.object_id
