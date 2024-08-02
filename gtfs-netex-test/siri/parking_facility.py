from dataclasses import dataclass, field

from .parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ParkingFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ParkingFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
