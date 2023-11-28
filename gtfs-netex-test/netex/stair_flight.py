from dataclasses import dataclass, field
from netex.stair_flight_versioned_child_structure import StairFlightVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StairFlight(StairFlightVersionedChildStructure):
    """
    SAn individual flight of a STAIR CASE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
