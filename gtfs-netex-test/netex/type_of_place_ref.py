from dataclasses import dataclass

from .type_of_place_ref_structure import TypeOfPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfPlaceRef(TypeOfPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
