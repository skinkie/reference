from dataclasses import dataclass, field
from typing import Optional
from netex.parking_bay_status_enumeration import ParkingBayStatusEnumeration
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayStatusValueStructure(TypeOfValueVersionStructure):
    """
    Type for a PARKING BAY STATUS.

    :ivar status: Current status
    """
    class Meta:
        name = "ParkingBayStatus_ValueStructure"

    status: Optional[ParkingBayStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
