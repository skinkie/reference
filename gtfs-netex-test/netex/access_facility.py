from dataclasses import dataclass, field

from .access_facility_enumeration import AccessFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessFacilityEnumeration = field(
        default=AccessFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
