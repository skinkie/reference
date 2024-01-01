from dataclasses import dataclass, field
from .reserved_space_facility_enumeration import (
    ReservedSpaceFacilityEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservedSpaceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ReservedSpaceFacilityEnumeration = field(
        default=ReservedSpaceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
