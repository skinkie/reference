from dataclasses import dataclass
from .type_of_journey_pattern_ref_structure import (
    TypeOfJourneyPatternRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfJourneyPatternRef(TypeOfJourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
