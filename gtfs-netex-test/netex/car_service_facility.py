from dataclasses import dataclass, field
from netex.car_service_facility_enumeration import CarServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CarServiceFacility:
    """
    Classification of CAR SERVICE FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CarServiceFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
