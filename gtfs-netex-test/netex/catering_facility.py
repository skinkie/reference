from dataclasses import dataclass, field
from .catering_facility_enumeration import CateringFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CateringFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CateringFacilityEnumeration = field(
        default=CateringFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
