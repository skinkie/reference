from dataclasses import dataclass, field
from netex.type_of_journey_pattern_value_structure import TypeOfJourneyPatternValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfJourneyPattern(TypeOfJourneyPatternValueStructure):
    """
    A classification of JOURNEY PATTERNs according to their functional purpose.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
