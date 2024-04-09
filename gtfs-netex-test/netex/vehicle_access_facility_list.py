from dataclasses import dataclass, field
from typing import List

from .vehicle_access_facility_enumeration import VehicleAccessFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleAccessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[VehicleAccessFacilityEnumeration] = field(
        default_factory=lambda: [
            VehicleAccessFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
