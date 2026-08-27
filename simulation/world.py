"""Air Aegis synthetic airspace simulation."""

from dataclasses import dataclass


@dataclass
class SimulatedObject:
    """A non-operational airborne object used by the simulator."""

    object_id: str
    x: float
    y: float
    altitude: float
    speed: float


def create_demo_object() -> SimulatedObject:
    """Create a deterministic demonstration object."""
    return SimulatedObject(
        object_id="OBJ-001",
        x=0.0,
        y=0.0,
        altitude=1000.0,
        speed=120.0,
    )


def advance_object(
    obj: SimulatedObject,
    dt: float,
) -> SimulatedObject:
    """Advance the simulated object using a simple constant-speed model."""
    if dt < 0:
        raise ValueError("dt must not be negative.")

    return SimulatedObject(
        object_id=obj.object_id,
        x=obj.x + obj.speed * dt,
        y=obj.y,
        altitude=obj.altitude,
        speed=obj.speed,
    )
