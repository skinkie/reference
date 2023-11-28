from dataclasses import dataclass, field
from netex.parking_bay_condition_version_structure import ParkingBayConditionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayCondition(ParkingBayConditionVersionStructure):
    """A record of the status of the PARKING BAY at a given moment in time.

    +v1.2.2

    :ivar id: Identifier of PARKING BAY STATUS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
