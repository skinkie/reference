from dataclasses import dataclass
from netex.type_of_place_ref_structure import TypeOfPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPlaceRef(TypeOfPlaceRefStructure):
    """
    Reference to a TYPE OF PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
