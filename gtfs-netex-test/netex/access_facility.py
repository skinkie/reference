from dataclasses import dataclass, field
from netex.access_facility_enumeration import AccessFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessFacility:
    """
    Classification of SITE  ACCESS FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessFacilityEnumeration = field(
        default=AccessFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
