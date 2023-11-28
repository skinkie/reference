from dataclasses import dataclass, field
from netex.pool_of_vehicles_version_structure import PoolOfVehiclesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PoolOfVehicles(PoolOfVehiclesVersionStructure):
    """A set of vehicles assigned to a specific PARKING, PARKING AREAs, PARKING
    BAYs, place or MOBILITY CONSTRAINT ZONE that must be  picked up and returned to
    the same area.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
