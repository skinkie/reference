from dataclasses import dataclass, field
from netex.vehicle_journey_layover_versioned_child_structure import VehicleJourneyLayoverVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyLayover(VehicleJourneyLayoverVersionedChildStructure):
    """A time allowance at the end of a specified VEHICLE JOURNEY.

    This time supersedes any global layover or JOURNEY PATTERN LAYOVER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
