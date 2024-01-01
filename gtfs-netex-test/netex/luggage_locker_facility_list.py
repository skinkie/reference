from dataclasses import dataclass, field
from typing import List
from .luggage_locker_facility_enumeration import (
    LuggageLockerFacilityEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageLockerFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[LuggageLockerFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
