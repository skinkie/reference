from dataclasses import dataclass, field

from .sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SanitaryFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SanitaryFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
