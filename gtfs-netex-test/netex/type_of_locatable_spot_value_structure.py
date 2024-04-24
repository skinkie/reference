from dataclasses import dataclass

from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLocatableSpotValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfLocatableSpot_ValueStructure"
