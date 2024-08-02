from dataclasses import dataclass, field

from .access_facility_enumeration import AccessFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AccessFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AccessFacilityEnumeration = field(
        default=AccessFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
