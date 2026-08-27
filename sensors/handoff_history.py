"""Track sensor handoff history for Air Aegis."""

from dataclasses import dataclass

from sensors.handoff import HandoffEvent


@dataclass
class HandoffHistory:
    """Store handoff events in chronological order."""

    events: list[HandoffEvent]

    def __init__(self) -> None:
        self.events = []

    def add(self, event: HandoffEvent) -> None:
        """Record a handoff event."""
        self.events.append(event)

    def latest(self) -> HandoffEvent | None:
        """Return the most recent handoff event."""
        if not self.events:
            return None

        return self.events[-1]

    def for_object(self, object_id: str) -> list[HandoffEvent]:
        """Return all handoffs for one simulated object."""
        return [
            event
            for event in self.events
            if event.object_id == object_id
        ]

    def __len__(self) -> int:
        """Return the number of recorded handoffs."""
        return len(self.events)
