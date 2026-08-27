from sensors.handoff import create_handoff
from sensors.handoff_history import HandoffHistory
from sensors.simulator import SimulatedSensor
from simulation.world import create_demo_object


def make_event(target_sensor: str):
    obj = create_demo_object()
    sensor = SimulatedSensor("SENSOR-01", random_seed=42)
    observation = sensor.observe(obj)

    return create_handoff(observation, target_sensor)


def test_history_starts_empty():
    history = HandoffHistory()

    assert len(history) == 0
    assert history.latest() is None


def test_history_records_events():
    history = HandoffHistory()

    history.add(make_event("SENSOR-02"))
    history.add(make_event("SENSOR-03"))

    assert len(history) == 2
    assert history.latest().target_sensor == "SENSOR-03"


def test_history_filters_by_object():
    history = HandoffHistory()

    event = make_event("SENSOR-02")
    history.add(event)

    matches = history.for_object(event.object_id)

    assert len(matches) == 1
    assert matches[0] is event
