from dataclasses import dataclass

from .addressable_place_ref_structure import AddressablePlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AddressablePlaceRef(AddressablePlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
