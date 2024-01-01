from dataclasses import dataclass, field
from .vehicle_access_facility_enumeration import (
    VehicleAccessFacilityEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleAccessFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: VehicleAccessFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
