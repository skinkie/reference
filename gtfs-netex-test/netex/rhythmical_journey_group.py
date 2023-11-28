from dataclasses import dataclass, field
from netex.rhythmical_journey_group_version_structure import RhythmicalJourneyGroupVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RhythmicalJourneyGroup(RhythmicalJourneyGroupVersionStructure):
    """A group of VEHICLE JOURNEYS following  the same JOURNEY PATTERN having the
    same "rhythm" every hour (for example runs all xxh10, xxh25 and xxh45...

    e) between a specified start and end time.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
