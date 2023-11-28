from dataclasses import dataclass, field
from netex.luggage_locker_facility_enumeration import LuggageLockerFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageLockerFacility:
    """
    Classification of LUGGAGE LOCKER FACILITY type.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LuggageLockerFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
