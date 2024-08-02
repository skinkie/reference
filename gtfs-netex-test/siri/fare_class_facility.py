from dataclasses import dataclass, field

from .fare_class_facility_enumeration import FareClassFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FareClassFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FareClassFacilityEnumeration = field(
        default=FareClassFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
