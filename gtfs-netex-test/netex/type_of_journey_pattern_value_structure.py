from dataclasses import dataclass

from .type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfJourneyPatternValueStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfJourneyPattern_ValueStructure"
