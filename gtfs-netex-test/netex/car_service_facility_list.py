from dataclasses import dataclass, field
from typing import List
from netex.car_service_facility_enumeration import CarServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CarServiceFacilityList:
    """
    List of CAR SERVICE FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[CarServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
