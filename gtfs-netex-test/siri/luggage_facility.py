from dataclasses import dataclass, field

from .luggage_facility_enumeration import LuggageFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LuggageFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: LuggageFacilityEnumeration = field(
        default=LuggageFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
