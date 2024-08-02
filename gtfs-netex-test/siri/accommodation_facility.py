from dataclasses import dataclass, field

from .accommodation_facility_enumeration import AccommodationFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AccommodationFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AccommodationFacilityEnumeration = field(
        default=AccommodationFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
