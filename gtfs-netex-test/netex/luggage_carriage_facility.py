from dataclasses import dataclass, field
from netex.luggage_carriage_enumeration import LuggageCarriageEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageCarriageFacility:
    """
    Classification of LUGGAGE CARRIAGE FACILITY type.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LuggageCarriageEnumeration = field(
        default=LuggageCarriageEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
