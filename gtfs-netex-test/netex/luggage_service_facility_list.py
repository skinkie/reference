from dataclasses import dataclass, field

from .luggage_service_facility_enumeration import LuggageServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LuggageServiceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[LuggageServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
