from dataclasses import dataclass, field

from .car_service_facility_enumeration import CarServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarServiceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CarServiceFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
