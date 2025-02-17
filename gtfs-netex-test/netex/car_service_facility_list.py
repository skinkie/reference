from dataclasses import dataclass, field

from .car_service_facility_enumeration import CarServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CarServiceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[CarServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
