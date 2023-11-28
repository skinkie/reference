from dataclasses import dataclass, field
from netex.parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingFacility:
    """
    Classification of PARKING FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ParkingFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
