from dataclasses import dataclass, field

from .refreshment_facility_enumeration import RefreshmentFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RefreshmentFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RefreshmentFacilityEnumeration = field(
        default=RefreshmentFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
