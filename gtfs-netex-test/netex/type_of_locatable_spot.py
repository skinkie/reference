from dataclasses import dataclass

from .type_of_locatable_spot_value_structure import TypeOfLocatableSpotValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfLocatableSpot(TypeOfLocatableSpotValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
