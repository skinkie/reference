from dataclasses import dataclass
from netex.type_of_journey_pattern_ref_structure import TypeOfJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfJourneyPatternRef(TypeOfJourneyPatternRefStructure):
    """
    Reference to a TYPE OF JOURNEY PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
