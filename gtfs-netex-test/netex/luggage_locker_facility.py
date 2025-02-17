from dataclasses import dataclass, field

from .luggage_locker_facility_enumeration import LuggageLockerFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LuggageLockerFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LuggageLockerFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
