from dataclasses import dataclass, field

from .mobility_facility_enumeration import MobilityFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MobilityFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: MobilityFacilityEnumeration = field(
        default=MobilityFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
