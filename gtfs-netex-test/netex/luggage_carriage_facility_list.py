from dataclasses import dataclass, field

from .luggage_carriage_enumeration import LuggageCarriageEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LuggageCarriageFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[LuggageCarriageEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
