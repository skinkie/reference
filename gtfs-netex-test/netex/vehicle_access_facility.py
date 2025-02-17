from dataclasses import dataclass, field

from .vehicle_access_facility_enumeration import VehicleAccessFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleAccessFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: VehicleAccessFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
