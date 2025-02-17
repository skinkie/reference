from dataclasses import dataclass, field

from .luggage_locker_facility_enumeration import LuggageLockerFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LuggageLockerFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[LuggageLockerFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
