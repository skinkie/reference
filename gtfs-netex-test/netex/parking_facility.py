from dataclasses import dataclass, field
from .parking_facility_enumeration import ParkingFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ParkingFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
